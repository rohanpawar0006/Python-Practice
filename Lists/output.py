
#(a)
list1 = [12,32,65,26,80,10]
list1.sort()
print(list1)

#(b)
list1 = [12,32,65,26,80,10]
sorted(list1)
print(list1)

#(c)
list1 = [1,2,3,4,5,6,7,8,9,10]
print(list1[::-2])
print(list1[:3] + list1[3:])

#(d)
list1 = [1,2,3,4,5]
print(list1[len(list1)-1])

#(e)
myList = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(myList)):
    if i%2 == 0:
        print(myList[i])

#(f)
myList = [1,2,3,4,5,6,7,8,9,10]
del myList[3:]
print(myList)

#(g)
myList = [1,2,3,4,5,6,7,8,9,10]
del myList[:5]
print(myList)

#(h)
myList = [1,2,3,4,5,6,7,8,9,10]
del myList[::2]
print(myList)

#(i)
list1 = [6,7,8,9]
print(list1 * 2)
#print(list1 *= 2)
#print(list1 =  list1 * 2)

#(j)
stRecord = ['Raman','A-36',[56,98,99,72,69],78.8]
print("Precentae: ", stRecord[3])
print("Marks in fifth subject is: ", stRecord[2][4])
print("Maximun marks: ", max(stRecord[2]))
print("Roll No: ", stRecord[1])
stRecord[0] = 'Raghav'
print("Name changed: ", stRecord[0])
