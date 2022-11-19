# Pair with Target Sum 

"""
Given an array of sorted numbers and a target sum, find a pair
in the array whose sum is equal to the given target

Write a function to return the indices of the two numbers such that they
add up to the given target

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""

def two_sum(nums, target):

	left = 0
	right = len(nums) - 1

	while left < right: 
		pair_sum = nums[left] + nums[right]
		if pair_sum > target:
			right -= 1
		elif pair_sum < target:
			left += 1
		else:
			return [left, right]

	return []


print(two_sum([1, 2, 3, 4, 6],6))
print(two_sum([2, 5, 9, 11],11))