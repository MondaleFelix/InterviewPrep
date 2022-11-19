# Squaring a Sorted Array

"""
Given a sorted array, create a new array containing
squares of all the numbers of the input array in the 
sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]


"""

def squaring_a_sorted_array(nums):

	left = 0
	right = len(nums) - 1
	sorted_array = []

	while left <= right:
		left_squared = nums[left] * nums[left]
		right_squared = nums[right] * nums[right]

		if right_squared > left_squared:
			sorted_array.append(right_squared)
			right -= 1
		else:
			sorted_array.append(left_squared)
			left += 1

	return sorted_array[::-1]

print(squaring_a_sorted_array([-2, -1, 0, 2, 3]))
print(squaring_a_sorted_array([-3, -1, 0, 1, 2]))
