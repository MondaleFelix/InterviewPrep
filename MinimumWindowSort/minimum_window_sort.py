# Problem Minimum Window Sort

"""

Problem Statement

Given an array, find the length of the smallest subarray
in it which when sorted will sort the whole array

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""

def minimum_window_sort(nums):

	left = 0
	right = len(nums) - 1

	while nums[left] < nums[left + 1] and left < len(nums) - 2:

		if left == len(nums) - 1:
			return 0
 
		left += 1

	while nums[right] > nums[right - 1] and right > 0:
		right -= 1


	min_number = nums[left]
	max_number = nums[right]

	for current_number in nums[left:right + 1]:
		min_number = min(min_number, current_number)
		max_number = max(max_number, current_number)

	# print(min_number, max_number)

	while min_number < nums[left - 1] and left > 0:
		left -= 1

	while max_number < nums[right] and right < len(nums) - 1:
		right += 1 

	return right - left + 1






print(minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(minimum_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(minimum_window_sort([1, 2, 3]))
print(minimum_window_sort([3, 2, 1]))












