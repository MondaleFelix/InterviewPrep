# Subarrays with Product Less than a Target 

"""

Problem Statement

Given an array with positive numbers and a postive target 
number, find all of its contiguous subarrays whose product 
is less than the target number

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10] ->6
Explanation: There are six contiguous subarrays whose product is less than the target.

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]  -> 7
Explanation: There are seven contiguous subarrays whose product is less than the target.


"""

def subarrays_with_product_less_than_target(nums, target):

	window_end = 0
	product = 1

	subs = []

	for window_start in range(len(nums)):
		window_end = window_start
		product *= nums[window_end]


		while product < target:
			window_end += 1
			subs.append(nums[window_start:window_end])

			if window_end == len(nums):
				break

			product *= nums[window_end]

		product = 1

	return subs





print(subarrays_with_product_less_than_target([2, 5, 3, 10],30))
print(subarrays_with_product_less_than_target([8, 2, 6, 5],50))

