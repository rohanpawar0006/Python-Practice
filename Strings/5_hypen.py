def hypenText(text):
    return text.replace(" ", "-")
    #return "-".join(text.split())


text = input("Enter the text: ")
result = hypenText(text)
print(f"New text with Hypen: {result}")
