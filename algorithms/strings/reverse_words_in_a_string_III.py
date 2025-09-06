"""
Source : https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
Author : Sonali Maharaj
Date   : 06/09/2025

****************************************************************************************************
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.

****************************************************************************************************
input: s (string)
output: s (string)
explanation: reverse the chars in each word in the string, keeping the order of words and ignoring whitespace, do not remove it
edgecases: 
pseudocode:

1. Split the string into words
2. reverse the characters in each word
3. join back the words with whitespaces
4. return the string


"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        