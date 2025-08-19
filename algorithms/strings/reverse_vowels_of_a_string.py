"""
Source : https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 19/08/2025

****************************************************************************************************

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

****************************************************************************************************
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []

        for v in s:
            if v in "aeiouAEIOU":
                vowels.append(v)
        
        vowels.reverse()

        s_list=list(s)
        i = 0

        for y in range(len(s_list)):
            if s_list[y] in "aeiouAEIOU":
                s_list[y] = vowels[i]
                i += 1
        
        return "".join(s_list)
