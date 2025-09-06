"""
Source : https://leetcode.com/problems/reverse-string/description/
Author : Sonali Maharaj
Date   : 06/09/2025

****************************************************************************************************
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

****************************************************************************************************

input: s (string)
output: s (string)
explanation: reverse the chars in the given string without using another string
edgecases: 
pseudocode:

1. set two variables, left for the beginning and right for the end of the string
2. swap the left char with the right char
3. increment the left var and decrement the right var
4. keep swapping until left==right


"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        