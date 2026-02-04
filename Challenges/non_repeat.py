"""
Challenge 4 (Continued): First Non-Repeating Element This is a very common interview problem, so we’ll be precise. Problem Recap
Goal
Read n integers
Find the first element that occurs exactly once
Maintain original order
If no such element exists → print
No unique element
Required Approach (DSA mindset)
You should use two passes:
Pass 1 → Build a frequency dictionary
Pass 2 → Traverse the list again and find the first element with frequency 1
"""
n = int(input("Enter number of elements: "))
numbers = dict()
for i in range(n):
    element = int(input("Enter element:"))
    if element in numbers:
        numbers[element] += 1
    else:
        numbers[element] = 1
found = False
for key, value in numbers.items():
    if value == 1:
        print(key)
        found = True
        break
if not found:
    print("No unqiue element")

""" 
n = int(input("Enter number of elements: "))
arr = []
freq = {}

for _ in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
    freq[num] = freq.get(num, 0) + 1

found = False
for num in arr:
    if freq[num] == 1:
        print(num)
        found = True
        break

if not found:
    print("No unique element")


Score: 7 / 10
Rubric:
Hashing logic: 9/10
Order handling: 5/10
Edge cases: 5/10
Interview readiness: 7/10
"""
