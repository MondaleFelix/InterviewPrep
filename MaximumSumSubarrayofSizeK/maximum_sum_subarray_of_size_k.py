# Maximum Sum Subarray of Size K (easy)

"""
Problem Statement 

Given an array of positive numbers and a positive number
'k', find the maximum sum of an contiguous subarray of size 'k'

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4]. 


"""

def max_sum_subarray_of_size_k(nums, k):

	window_sum = 0
	window_start = 0
	max_sum = 0

	for window_end in range(len(nums)):
		window_sum += nums[window_end]

		if window_end >= k-1:
			max_sum = max(max_sum,window_sum)
			window_sum -= nums[window_start]
			window_start += 1

	return max_sum

print(max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2],3))
print(max_sum_subarray_of_size_k([2, 3, 4, 1, 5],2))