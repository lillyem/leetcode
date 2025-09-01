"""
Source : https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 01/09/2025

****************************************************************************************************

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

****************************************************************************************************

input: nums (int array), k (int)
output: max avg (float)
explanation: find a subarray with length k to give the max avg value
edgecases: nums has 1 element, k is 1
pseudocode:

1. create k_sum variable to track sum in window
2. get the sum of the first window in the array, set it to k_sum
3. set max_sum to be k_sum, the sum of the first window
4. for each following window, find the k_sum, see if it is greater than existing max_sum, if it is, replace max_sum
5. return the rounded average 

"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        k_sum = 0
        for i in range(k):
            k_sum += nums[i]
        
        max_sum = k_sum

        for i in range(k, len(nums)):
            k_sum += nums[i] - nums[i - k]
            if k_sum > max_sum:
                max_sum = k_sum

        max_avg = float(max_sum) / k

        return round(max_avg,5)
