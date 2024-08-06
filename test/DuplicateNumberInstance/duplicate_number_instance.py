"""
Find Non-Duplicate Number Instances (easy)


Problem Statement
Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place. The non-duplicate numbers should be sorted and you should not use any extra space so that the solution has constant space complexity i.e., .

Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Example 1:
                 L       R
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after moving element will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after moving elements will be [2, 11].


"""

def non_duplicate_number_instance(nums):

	left = 0 
	right = 1

	while right <= len(nums) - 1:
		l_number = nums[left]
		r_number = nums[right]

		if l_number != r_number:
			nums[left + 1], nums[right] = nums[right], nums[left + 1]
			left += 1
			right += 1
		else:
			right += 1


	return left + 1



print(non_duplicate_number_instance([2, 3, 3, 3, 6, 9, 9]))
print(non_duplicate_number_instance([2, 2, 2, 11]))