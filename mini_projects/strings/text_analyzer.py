# Text Analyzer

text = input("Enter a sentence: ")

print("Characters:", len(text))
print("Words:", len(text.split()))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

vowels = 0
consonants = 0
digits = 0

for i in text:
    if i.lower() in "aeiou":
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i.isdigit():
        digits += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)

word = input("Enter a word to search: ")

if word.lower() in text.lower().split():
    print("Word found")
else:
    print("Word not found")
