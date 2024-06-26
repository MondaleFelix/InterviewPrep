# Triplets with Smaller Sum

"""

Problem Statement

Given an array arr of unsorted numbers and a target sum,
count all triplets in it such that 
arr[i] + arr[j] + arr[k] < target where i, j, and k are 
three different indices. Write a function to 
return the count of such triplets.

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum
is less than the target: [-1, 0, 3], [-1, 0, 2]

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is 
less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
 

"""

def triplets_with_smaller_sum(nums, target):

	nums.sort()
	triplet_count = 0

	for i in range(len(nums) - 2):
		left = i + 1
		right = len(nums) - 1

		while left <= right:
			triplet_sum = nums[i] + nums[left] + nums[right]

			if triplet_sum > target:
				right -= 1
			else:
				triplet_count += 1
				left += 1

	return triplet_count

print(triplets_with_smaller_sum([-1, 0, 2, 3], 3))
print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))





