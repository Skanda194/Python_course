# #. Find all anagrams in a string
#
# Problem
# Given two strings `s` and `p`, return all starting indices of `p`'s anagrams in `s`.
# An anagram is a rearrangement of characters using the same frequency.
#
# What you need to do
# Slide a window of size `len(p)` over `s` and check where character frequencies match `p`.
#
# Example 1
# Input
# s = "cbaebabacd"
# p = "abc"
#

# Output
# [0, 6]
#
# Explanation
# "cba" at index 0 is an anagram of "abc"
# "bac" at index 6 is an anagram of "abc"
#
# Example 2
# Input
# s = "abab"
# p = "ab"
#
# Output
# [0, 1, 2]
#
# Explanation
# "ab", "ba", "ab" are all anagrams
#
# ---
#
#  2. Group words by length
#
# Problem
# Given a list of words, group them based on their length.
#
# What you need to do
# Create groups where all words of the same length are together.
#
# Example 1
# Input
# ["go", "cat", "bat", "hi", "dog"]
#
# list=["hi", "my", "name","is","skanda" ]
# grouped={}
# for word in list:
#     grouped.setdefault(len(word),[]).append(word)
# for length in sorted(grouped):
#     print(f"{length}:{', '.join(grouped[length])}")
# Output
# {
# 2: ["go", "hi"],
# 3: ["cat", "bat", "dog"]
# }
#
# Example 2
# Input
# ["a", "ab", "abc", "de", "f"]
#
# Output
# {
# 1: ["a", "f"],
# 2: ["ab", "de"],
# 3: ["abc"]
# }
#
# ---
#
#  3. Reverse words in a string
#
# Problem
# Given a string, reverse the order of words.
#
# What you need to do
# Words remain same, only order changes.
#
# Example 1
# Input
# "the sky is blue"
#
# Output
# "blue is sky the"
#
# Example 2
# Input
# "hello world python"
#
# Output
# "python world hello"
# def reverse_words(text):
#     words=text.split()
#     rev_words=words[::-1]
#     return " ".join(rev_words)
# print(reverse_words("hi how are you"))
# ---
#
#  4. Find all duplicates in a list
#
# Problem
# Given a list of integers, return all elements that appear more than once.
#
# What you need to do
# Identify numbers that occur multiple times. Return unique duplicates.
#
# Example 1
# Input
# [1, 2, 3, 1, 3, 6, 6]
#
# Output
# [1, 3, 6]
#
# Example 2
# Input
# [4, 5, 6, 7, 4, 8, 5]
#
# Output
# [4, 5]
# def find_duplicates(nums):
#     seen=set()
#     duplicates=set()
#     for num in nums:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)
#     return list(duplicates)
#
# myList=[10,20,30,40,50,60,70,70,70,80,80,80,90,90,10,10]
# print(find_duplicates(myList))
# ---
#
#  5. Find the missing number from 1 to n
#
# Problem
# Given an array containing numbers from 1 to n with one number missing, find the missing number.
def findmissingnumber(nums):
    n=len(nums)+1
    expectedsum= n*(n+1)//2
    actualsum=sum(nums)
    return expectedsum - actualsum
list=[1,2,3,5]
print(findmissingnumber(list))
# What you need to do
# Numbers range from 1 to n. Exactly one number is missing.
#
# Example 1
# Input
# [1, 2, 4, 5]
#
# Output
# 3
#
# Explanation
# Numbers should be 1 to 5. Missing number is 3.
#
# Example 2
# Input
# [2, 3, 1, 5]
#
# Output
# 4
#
# Explanation
# Numbers should be 1 to 5. Missing number is 4.