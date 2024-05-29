"""

Number of Good Pairs (easy)
Problem Statement
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
			         L   R
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs, here are the indices: (0,3), (0,4), (3,4), (2,5).
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array is a 'good pair'.
Example 3:

Input: words = nums = [1,2,3]
Output: 0
Explanation: No number is repeating.




"""

def number_of_good_pairs(nums):

	pair_count = 0
	seen = {}

	for number in nums:
		if number in seen:
			pair_count += seen[number]
			seen[number] += 1
		else:
			seen[number] = 1

	return pair_count


print(number_of_good_pairs([1,2,3,1,1,3]))
print(number_of_good_pairs([1,1,1,1]))
print(number_of_good_pairs([1,2,3]))





