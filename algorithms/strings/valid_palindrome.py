"""
Source : https://leetcode.com/problems/valid-palindrome/description/
Author : Sonali Maharaj
Date   : 06/09/2025

****************************************************************************************************
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

****************************************************************************************************
input: s (string)
output: bool
explanation: checking if a string reads the same forward and backwards after removing all non-alphanumeric chars 
edgecases: the string is one space, if s is one char
pseudocode:

1. convert all uppercase into lowercase
2. only keep character in string if it is alnum
3. push each character of string into stack
4. pop stack and compare each letter with original string, if it doesn't match, immediately return false
5. return true 

# or use two pointer 

#if we do it in one loop, skip on the left & right if not alnum
1. convert all uppercase into lowercase
2. only keep character in string if it is a alnum
3. compare the leftmost and rightmost chars, return false if it doesn't match
4. if it is a match, increment left and decrement right, continue comparison
5. return true at the end after all comparisons completed

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        