"""
Source : https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 28/08/2025

****************************************************************************************************
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


****************************************************************************************************

input: nums (integer array)
output: bool (true/false)
explanation: check indices i,j,k to see if nums[i] < nums[j] < nums[k]
edge cases: no triplet, nums length < 3
psuedocode:

1. create two variables to track qualfied i's & j's
2. set the next element in nums to i 
3. once i is set, the next number that is greater than i, becomes j
4. the next number that is greater than j, becomes k and we return true
5. if none is true, return false
            
            

"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3:
            return False

        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else: 
                return True

        return False
            
