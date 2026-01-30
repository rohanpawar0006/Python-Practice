def deleteChar(text, char):
    new_text = text.replace(char, "")
    return new_text

text = input("Enter the Text: ")
char = input("Enter the Character to delete: ")
result = deleteChar(text, char)
print(f"The text after deleting the {char} Character: {result}")

'''
def deleteChar(text, char):
    result = ""
    for ch in text:
        if ch != char:
            result += ch
    return result
'''