# Separate Duplicates

"""
Problem Statement

Given an array of sorted numbers, remove all duplicate number 
instances from it in-place, such that each element appears 
only once. The relative order of the elements should be kept 
the same and you should not use any extra space so that that 
the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and 
after moving return the length of the subarray that has no 
duplicate in it.


Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

def separate_duplicates(nums):

	sorted_index = 1

	for i in range(len(nums) - 1):
		if nums[i] != nums[i + 1]:
			nums[i] = nums[sorted_index]
			sorted_index += 1


	return sorted_index



print(separate_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(separate_duplicates([2, 2, 2, 11]))