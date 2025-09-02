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


1. you have left and right variables to track the window, a max_ones variable to track the max number of 1s and a zero_count to track the zeroes in a window
2. once the element is equal to 0, increment zero_count 
3. while the zero_count > 1, when you slide the window, if the value at left is zero, minus 1 from the zero_count
4. update the max_ones to be biggest value between itself and right - left
5. return max_ones

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
