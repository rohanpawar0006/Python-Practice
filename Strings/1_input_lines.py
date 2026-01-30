text = input("Enter the sentence: ")
character = (len(text))
alphabets = 0
digits = 0
specia_symbols = 0

for i in text:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    elif i != " ":
        specia_symbols += 1

if text.strip() == "":
    words = 0
else:
    words = text.count(" ") + 1
    
print("Total Number of Characters in your text are: ", character)
print("Total Number of Alphabets in your text are: ", alphabets)
print("Total Number of Digits in your text are: ", digits)
print("Total Number of Specail Symbols in your text are: ", specia_symbols)
print("Total Number of Words in your text are: ", words)
