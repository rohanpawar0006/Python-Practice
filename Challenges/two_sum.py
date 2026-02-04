"""
Challenge 7: Pair With Given Sum (Two Sum Pattern)
This is a core interview problem. If you master this, you unlock many variations.
Problem
Goal
Write a function:
def has_pair_with_sum(arr, target):
That returns:
True → if any two distinct elements in the array sum to target
False → otherwise
Rules / Constraints
Use:
set or dict
❌ No nested loops
❌ No sorting
Time complexity must be O(n)
How to Think (Interview Mindset)
For each number x:
You need target - x
If you’ve already seen it → pair exists
"""
def has_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        needed = target - num
        if needed in seen:
            return True
        seen.add(num)
    return False
n = int(input("Enter the number of element: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter element: ")))
target = int(input("Enter the Target to find: "))
result = has_pair_with_sum(numbers, target)
print(result)

""" 
Score: 6.5 / 10
Rubric:
Idea understanding: 8.5/10
Correctness: 5/10
Constraint adherence: 5.5/10
Interview readiness: 6.5/10
"""
