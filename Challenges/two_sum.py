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