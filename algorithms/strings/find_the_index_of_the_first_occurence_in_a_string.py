"""
Source : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
Author : Sonali Maharaj
Date   : 06/09/2025

****************************************************************************************************
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

****************************************************************************************************
input: needle (string), haystack (string)
output: index (int)
explanation: find the first occurence of the first string in the second string
edgecases: if needle is longer than haystack
pseudocode:

1. go through the haystack string and compare each character with the chars in needle string
2. if the first index is a match, store it
3. if all are found, in order, return the index of the first character of the word in the haystack
4. if not found, continue searching in the haystack string until the end
5. if not found at all, return -1

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
            