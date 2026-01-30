#(a)
a = 110
while a > 100:
    print(a)
    a -= 2

#(b)
for i in range (20, 30, 2):
    print(i)

#(c)
country = 'INDIA'
for i in country:
    print(i)

#(d)
i = 0
sum = 0
while i < 9:#
    if i % 4 == 0:
        sum = sum + i
    i = i + 2
print(sum)

#(e)
for x in range (1, 4):
    for y in range(2, 5):
        if x * y > 10:
            print (x * y)
            break

#(f)
var = 7
while var > 0:
    print('Current variable value: ', var)
    var = var - 1
    if var == 3:
        break
    else:
        if var == 6:
            var = var - 1
            continue
    print("Good Bye!")
