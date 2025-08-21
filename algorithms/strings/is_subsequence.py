"""
Source : https://leetcode.com/problems/is-subsequence?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 19/08/2025

****************************************************************************************************

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

****************************************************************************************************
UMPIRE: 

input: s (str), t (str)

output: bool

explanation: 

-check if s is a subsequence of t, that is s contains some (or all) of the characters in t in the order it appears in t

edge cases:

1. letters in s are from t, in order -> a new string can be formed
2. s has 0 chars
3. t has 0 chars

two pointer- keep two indexes for the array you're working on

s = abc
t = ahbgdc

psuedocode:

i = 0 #this is for s
j = 0 #this is for t

for j in range(length of t):
    if t[j] == s[i]
        i+=1

    elif t[j] not == s[i]
        continue

if i is equal to s.length return true

else return false


Time complexity 

O(n)

"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i = 0 #tracking s
        j = 0 #tracking t

        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        for j in range(len(t)):
            if t[j]==s[i]:
                i += 1

                if i >= len(s):
                    return True 

            elif t[j] != s[i]:
                continue
        
        if i==len(s):
            return True

        return False
