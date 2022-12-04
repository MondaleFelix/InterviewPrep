# Container With Most Water

"""
Problem Statement

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container,
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49       0 1 2 3 4 5 6 7 8
Explanation: The above vertical lines are represented by 
array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water 
(blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

"""

def container_with_most_water(nums):
    left = 0
    right = len(nums) - 1

    max_area = 0

    while left < right:

        l_container = nums[left]
        r_container = nums[right]

        area = min(l_container, r_container) * (right - left)

        max_area = max(area, max_area)


        if l_container > r_container:
            right -= 1
        elif r_container < l_container:
            left += 1
        else:
            left += 1

    return max_area

print(container_with_most_water([1,8,6,2,5,4,8,3,7]))
print(container_with_most_water([1,1]))