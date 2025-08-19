"""
Source : https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 19/08/2025

****************************************************************************************************

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

****************************************************************************************************
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """   
        count = 0
        length = len(flowerbed)

        for i in range(length):
            
            #if plot is empty
            if flowerbed[i] == 0:
                
                #check if it is the first plot or if the plot before is empty
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                
                #check if it is the last plot or if the plot after is empty
                empty_right = (i == length - 1) or (flowerbed[i+1] == 0)
                
                #if the left and right are empty, plant the flower and increase the count 
                if empty_left and empty_right:
                    flowerbed[i] = 1  
                    count += 1

                    #check if count is greater than or equal to the number 
                    #of flowers we have to plant 
                    #if it is, we can return true since we planted all successfully
                    if count >= n:    
                        return True

        return False
