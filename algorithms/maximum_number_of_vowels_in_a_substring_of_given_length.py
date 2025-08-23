"""
Source : https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 23/08/2025

****************************************************************************************************

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length


****************************************************************************************************

input:

1. s = str
2. k = integer

output:

1. max_vowel= int

explanation:

find the max num of vowels in any substring of length k in a given string
use sliding window method


edge cases:
1. all letters are vowels
2. no vowels 
3. k=1

pseudocode:

vowels = set("aeiou")

vowel_count = 0
max_vowels = 0 

for i in range(k):
    if s[i] is a vowel:
        increment vowel_count

max_vowels = vowel_count

for i in range k to length of s:

    if the first char from the last window is a vowel:
        decrement vowel_count 

    if last char from the new window is a vowel:
        increment vowel_count 
    
    max_vowels = maximum between max_vowels and vowel_count

return max_vowels


"""
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set("aeiou")

        vowel_count = 0
        max_vowels = 0 

        for i in range(k):
            if s[i] in vowels:
                vowel_count+=1
        
        max_vowels = vowel_count

        for i in range (k, len(s)):

            if s[i-k] in vowels:
                vowel_count -= 1

            if s[i] in vowels:
                vowel_count += 1
            
            max_vowels = max(max_vowels, vowel_count)

        return max_vowels
