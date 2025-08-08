import logging
import pytesseract
import pandas as pd
from PIL import Image
from io import BytesIO
from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- Настройки ---
TOKEN = "8241301296:AAFjU5qNH5FtSFP4Rkl4eBkwGVK_4DIKblw"  # токен от @BotFather
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # путь к Tesseract на Windows

# --- Логирование ---
logging.basicConfig(level=logging.INFO)

# --- Файл для хранения данных ---
EXCEL_FILE = "spending.xlsx"

# --- Команда /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне фото чека, и я сохраню его в таблицу.")

# --- Обработка фото ---
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    img_bytes = await file.download_as_bytearray()

    # Распознаем текст
    img = Image.open(BytesIO(img_bytes))
    text = pytesseract.image_to_string(img, lang="eng+rus")

    # --- Минимальный парсинг ---
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    shop = "Неизвестно"
    total = None

    for line in text.split("\n"):
        if "Магазин" in line or "Shop" in line:
            shop = line.strip()
        if "ИТОГО" in line.upper() or "TOTAL" in line.upper():
            total = ''.join(ch for ch in line if ch.isdigit() or ch == ".")
    
    # --- Сохраняем в Excel ---
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Дата", "Магазин", "Сумма", "Текст чека"])

    df = pd.concat([df, pd.DataFrame([[date, shop, total, text]], columns=df.columns)])
    df.to_excel(EXCEL_FILE, index=False)

    await update.message.reply_text(f"Чек сохранён!\nМагазин: {shop}\nСумма: {total if total else 'Не найдено'}")

# --- Отчёт ---
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        await update.message.reply_text("Нет данных.")
        return

    total_spent = df["Сумма"].dropna().astype(float).sum()
    await update.message.reply_text(f"За всё время потрачено: {total_spent:.2f} руб/долларов.")

# --- Запуск ---
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("report", report))
app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

if __name__ == "__main__":
    app.run_polling()