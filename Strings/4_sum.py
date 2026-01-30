def sumNum(text):
    sum1 = 0
    for i in text:
        if i.isdigit():
            sum1 += int(i)
    return sum1

text = input("Enter the text: ")
Total = sumNum(text)
print("The Total Sum of digits in text is: ", Total)
