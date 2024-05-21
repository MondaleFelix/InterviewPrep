"""

Problem Statement 

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct

Example 1:

Input: nums= [1, 2, 3, 4]
Output: false  
Explanation: There are no duplicates in the given array.

Example 2:

Input: nums= [1, 2, 3, 1]
Output: true  
Explanation: '1' is repeating.


"""

def contains_duplicate(nums):
	seen = {}

	for number in nums:
		if number in seen:
			return True
		seen[number] = True
	return False

print(contains_duplicate([1, 2, 3, 4])) # False
print(contains_duplicate([1, 2, 3, 1])) # True

























