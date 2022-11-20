# Triplet Sum to Zero

"""
Problem Statement

Given an array of unsorted numbers, find all unique triplets
in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.



"""

def triplet_sum_to_zero(nums):

	nums.sort()
	triplets = []

	for i in range(len(nums) - 2):

		if nums[i] == nums[i - 1]:
			continue

		left = i + 1
		right = len(nums) - 1

		while left < right:
			triplets_sum = nums[i] + nums[left] + nums[right]

			if triplets_sum == 0:
				triplets.append([nums[i], nums[left], nums[right]])
				right -= 1
				left += 1

				while nums[left] == nums[left - 1]:
					left += 1

				while nums[right] == nums[right + 1]:
					right -= 1

			elif triplets_sum > 0:
				right -= 1
			else:
				left += 1

	return triplets

print(triplet_sum_to_zero([-3, 0, 1, 2, -1, 1, -2]))			
print(triplet_sum_to_zero([-5, 2, -1, -2, 3]))			



