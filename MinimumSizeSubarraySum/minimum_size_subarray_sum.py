# Minimum Size Subarray Sum

"""
Given an array of positive numbers and a postive integer target,
return the minimal length of a subarray whose sum is greater 
than or equal to target. If there is no such subarray, return 0 instead

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Input: target = 4, nums = [1,4,4]
Output: 1

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


"""

def minimum_sum_subarray_sum(nums, target):

	window_start = 0 
	window_sum = 0
	min_length = len(nums) + 1

	for window_end in range(len(nums)):

		window_sum += nums[window_end]

		while window_sum >= target:
			min_length = min(min_length, window_end - window_start + 1)
			window_sum -= nums[window_start]
			window_start += 1

	if min_length == len(nums) + 1:
		return 0

	return min_length

print(minimum_sum_subarray_sum([2,3,1,2,4,3],7))
print(minimum_sum_subarray_sum([1,4,4],4))
print(minimum_sum_subarray_sum([1,1,1,1,1,1,1,1],11))