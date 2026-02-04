"""
Challenge 9: Strings + Hashing (Very Common)
Problem: Check if Two Strings Are Anagrams
Goal
Write a function:
def are_anagrams(s1, s2):
That returns:
True if s1 and s2 are anagrams
False otherwise
Rules / Constraints
Ignore spaces
Case-insensitive
❌ Do NOT use sorted()
Use:
dict or set
Time complexity: O(n)
"""
def are_anagrams(s1, s2):
    counts1, counts2 = {}, {}
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
        counts2[s2[i]] = 1 + counts2.get(s2[i], 0)
    for i in counts1:
        counts1[i] != counts2[i]
        return False
    return True
s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
print(are_anagrams(s1, s2))
