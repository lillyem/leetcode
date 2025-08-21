"""
Source : https://leetcode.com/problems/container-with-most-water?envType=study-plan-v2&envId=leetcode-75
Author : Sonali Maharaj
Date   : 19/08/2025

****************************************************************************************************

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

****************************************************************************************************
UMPIRE: 

input: 

1. height: array (int) of length n

output:

1. max_water (int)

thoughts:


start with pointers at the first column (left) and last column (right)
if the left height <= right height increment left
if the left height >= right height decrement right
ensure the left pointer remains < right pointer
height will be minimum of the left and right column
calculate area and store max
exit when left=right


explanation:

find the two columns that allow you to find the max area rectangle

edge cases:

1. n=2, compute area immediately
2. n>2, a soln can be formed
3. height[i]=0 #not sure 

pseudocode:

left_column = 0
right_column = length of height array - 1
max_water = 0

while left is not equal to right

    height = minimum of left height and right height
    width = right - left
    area = height x width
    max_water = maximum of max_water and area 

    if the left height <= right height 
        increment left
    elif the left height >= right height 
        decrement right

return the max water

"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height)-1
        max_water = 0

        #since we are incrementing the left and decrementing the right
        #we can exit if the left==right column

        while left != right:
            
            #height is the min of the two columns since water spills over
            water_height = min(height[left], height[right])
            width = right - left
            area = water_height * width

            max_water = max(max_water,area)

            #increment/decrement the shorter of the two columns as necessary
            if height[left] <= height[right]:
                left+=1
            elif height[left] >= height[right]: 
                right-=1

        #after while loop exits, simply return the max value of water
        return max_water
