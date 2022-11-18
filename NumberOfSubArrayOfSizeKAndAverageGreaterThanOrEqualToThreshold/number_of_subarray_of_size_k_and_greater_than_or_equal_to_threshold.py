# Number of Subarray of Size K and Average Greater Than Or Equal to Threshold

"""
Given an array of integers arr and two integers K and Threshold,
return the number of sub-arrays of size k and average greater than or equal
to threshold

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


"""

def num_of_subarray_of_size_k_and_average_greater_than_or_equal_to_threshold(arr, k, threshold):

	window_sum = 0
	window_start = 0
	subarray_count = 0

	for window_end in range(len(arr)):

		window_sum += arr[window_end]

		if window_end >= k - 1:
			average = window_sum / k

			if average >= threshold:
				subarray_count += 1

			window_sum -= arr[window_start]
			window_start += 1

	return subarray_count

print(num_of_subarray_of_size_k_and_average_greater_than_or_equal_to_threshold([2,2,2,2,5,5,5,8],3,4))
print(num_of_subarray_of_size_k_and_average_greater_than_or_equal_to_threshold([11,13,17,23,29,31,7,5,2,3],3,5))
