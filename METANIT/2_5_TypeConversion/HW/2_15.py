'''
global
nonlocal
outer()
inner()
Замыкание (closure) представляет функцию, которая запоминает свое лексическое окружение даже в том случае, когда она выполняется вне своей области видимости.

### Область видимости в Python

В Python существует несколько областей видимости, которые определяют, где можно использовать переменные. Вот основные области видимости:

1. **Local (локальная)** - внутри функции.
2. **Enclosing (вложенная)** - внутри функции, содержащей другую функцию.
3. **Global (глобальная)** - на уровне модуля (файла).
4. **Built-in (встроенная)** - предопределенные функции и имена.

### Ключевое слово `global`

Ключевое слово `global` позволяет изменять глобальные переменные внутри функции. Без него, присваивание значения переменной внутри функции создаст новую локальную переменную. Пример:

```python
x = 10

def change_global():
    global x
    x = 20

change_global()
print(x)  # Вывод: 20
'''