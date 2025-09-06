"""
Source : https://leetcode.com/problems/reverse-string-ii/description/
Author : Sonali Maharaj
Date   : 06/09/2025

****************************************************************************************************
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104

****************************************************************************************************

nput: s (string), k (int)
output: s (string)
explanation: for an integer k eg k=2, and a string, reverse the k characters, then skip the next k chars and reverse the next k chars, if >k chars left, reverse all, if <2k but >=k, reverse the first k chars and leave the rest

edgecases: 
pseudocode:

1. for the first 2k chars, reverse the first k chars
2. move to the next group of 2k chars
3. if there is less than k chars left, reverse all
4. if there is less than 2k but  greater than or equal to k, reverse the first k chars 
5. return the final string


"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        