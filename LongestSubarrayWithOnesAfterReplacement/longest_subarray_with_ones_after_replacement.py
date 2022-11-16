# Longest Subarray with Ones after Replacement

"""
Problem Statement

Given an array containing 0s and 1s, if you are allowed to 
replace no more than ‘k’ 0s with 1s, find the length of the
longest contiguous subarray having all 1s.

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.


"""

def longest_subarray_with_ones_after_replacement(nums, k):

	zero_count = 0
	window_start = 0
	max_length = 0

	for window_end in range(len(nums)):

		right_num = nums[window_end]

		if nums[window_end] == 0:
			zero_count += 1

		while zero_count > k:
			left_number = nums[window_start]
			if left_number == 0:
				zero_count -= 1

			window_start += 1

		max_length = max(max_length, window_end - window_start + 1)

	return max_length


print(longest_subarray_with_ones_after_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],2))
print(longest_subarray_with_ones_after_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],3))


