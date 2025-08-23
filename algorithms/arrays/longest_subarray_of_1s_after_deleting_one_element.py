"""
Source : https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
Author : Sonali Maharaj
Date   : 23/08/2025

****************************************************************************************************
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


input: 

1. nums: int array (binary)


output:

1. size of the longest non-empty subarray: integer

explanation:

find the subarray with the max number of ones 
use the sliding window approach

edgecases: 

1. all elements are 1
2. all elements are zero


pseudocode:

left = 0       #track the start of the window
zero_count = 0      
max_ones = 0     

for right in range(length of nums):
    if nums at right is zero:
        increment zero count

    while zero count is greater than one:
        if nums at left is zero:
            decrement zero count #since we're gonna slide the window
        increment the left count #slide the window, move the left pointer forward by one
            
            
    max_ones = max of max_ones and right index - left index 

return max_ones


****************************************************************************************************
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0       
        zero_count = 0      
        max_ones = 0     

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

        
            max_ones = max(max_ones, right - left)

        return max_ones
