"""
Source : https://leetcode.com/problems/product-of-array-except-self/submissions/1741461139/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 21/08/2025

****************************************************************************************************

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


****************************************************************************************************
UMPIRE: 

input:

1.nums (integer array)

output:

2.answer (integer array)

explanation:

- find the product of all integers in the array except itself 
- algorithm must run in O(n)

edge cases:

-nums[i]=0
-nums length is 2

pseudocode:

n = length of nums
answer = array of size n, initialized with 1

prefix = 1
for i from 0 to n-1:
    answer[i] = prefix
    prefix = prefix * nums[i]

suffix = 1
for i from n-1 down to 0:
    answer[i] = answer[i] * suffix
    suffix = suffix * nums[i]

return answer


for the first for loop: 
#1. answer[i] = 1, prefix = 1, answer = [1 ,1, 1, 1]
#2. answer[i] = 1, prefix = 2, answer = [1, 1, 1, 1]
#3. answer[i] = 2, prefix = 6, answer = [1, 1, 2, 1]
#4. answer[i] = 6, prefix = 24, answer = [1, 1, 2, 6]

for the second for loop:
#1. answer[i] = 6, suffix = 4, answer = [1, 1, 2, 6]
#2. answer[i] = 8, suffix = 12, answer=  [1, 1, 8, 6]
#3. answer[i] = 12, suffix = 24, answer = [1, 12, 8, 6]
#4. answer[i] = 24, suffix = 24, answer = [24, 12, 8, 6]

"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
