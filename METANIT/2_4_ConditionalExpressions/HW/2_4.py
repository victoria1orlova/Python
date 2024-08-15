#Checking for vowels in a string

text = "Hello, world!"
vowels = "aeiou"
contains_vowel = False
for char in text:
    if char in vowels:
        contains_vowel = True  # Set to True if a vowel is found
print("Contains vowels:", contains_vowel)
