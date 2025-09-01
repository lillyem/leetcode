"""
Source : https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 28/08/2025

****************************************************************************************************

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.


****************************************************************************************************


input: chars [] 
output: chars []
explanation: count the instances of the same char and compress it in the same array with the char and number of that char after
edgecases: array has 1 char, array has one of each char
pseudocode:

1. Initialize write = 0 and count = 1.
2. Loop through the array from the second character to the end, counting consecutive characters.
3. When the current character is different from the previous or at the end, write the previous character and its count (if >1) into the array at write, then reset count = 1.
4. Return write as the new length of the compressed array.

"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        write = 0
        count = 1     

        for i in range(1, len(chars) + 1):  
           
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            else:
                
                chars[write] = chars[i - 1]
                write += 1

                
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1

                count = 1   

        return write
