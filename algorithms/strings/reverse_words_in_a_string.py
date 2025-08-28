"""
Source : https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 28/08/2025

****************************************************************************************************
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

****************************************************************************************************

input: s (string)
output: s (string) - reversed 
explanation: reverse the order of words in the string
edge cases: one word in string, two words in string

pseudocode:

#helper function to break string up into words

def split_word(s):
    result=[]
    word=''

    for c in s:
        if c is not a space, tab or newline:
            word+=c 
            #keep adding c to word, else append word to result

        elif word:
            append word to result
            reset word to be empty
    if word:
        append last word to result

    return result

def reverse_array(s):

    left=0
    right=len(s)-1

    while left<right:
        swap s at left with s at right
        increment left and decrement right
    return s


#call functions 

string_array = split string into words
reverse_string_array= reverse words array

new_string = convert array into string 

return new_string

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def split_word(s):
            result=[]
            word=''

            for c in s:
                if c not in [' ', '\t', '\n']:
                    word+=c
                elif word:
                    result.append(word)
                    word=''
            if word:
                result.append(word)

            return result

        def reverse_array(s):

            left=0
            right=len(s)-1

            while left<right:
                temp=s[right]
                s[right]=s[left]
                s[left]=temp
                left+=1
                right-=1
            return s


        string_array = split_word(s)
        reverse_string_array=reverse_array(string_array)

        new_string = " ".join(reverse_string_array)

        return new_string
