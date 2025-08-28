"""
Source : https://leetcode.com/problems/move-zeroes/description/
Author : Sonali Maharaj
Date   : 28/08/2025

****************************************************************************************************

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

****************************************************************************************************

input: 

1. nums: integer array

output: 

1. nums: integer array

explanation:

move all nums[i] that are == 0 to the right of the array without using another array and maintaining
the order of the non-zero elements

edge cases: 

1.nums = [0]
2. nums has two elements

pseudocode:

left = 0
        
for right in range(length of nums):

    if nums at right != 0:


        temp = nums at right
        nums at right right = nums at left 
        nums at left = temp


        incrememnt left #if nums at right isn't zero

    return nums
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        for right in range(len(nums)):

            if nums[right] != 0:

        
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp


                left += 1

       
