# Quadruple Sum To Target

"""
Problem Statement

Given an array od unsorted numbers and a target number, find
all unique quadruplets in it, whose sum is equal to the target
number

Input: [4, 1, 2, -1, 1, -3], target=1
	   [-3, -1, 1, 1, 2, 4]


Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.


"""

def quadruple_sum_to_target(nums, target):

	nums.sort()
	quads = []

	for i in range(len(nums) - 3):
		if i > 0 and nums[i] == nums[i -1]:
			continue

		for j in range(i + 1,len(nums) - 2):
			if j > i + 1 and nums[j] == nums[j - 1]:
				continue

			left = j + 1
			right = len(nums) - 1

			while left < right:
				quad_sum = nums[i] + nums[j] + nums[left] + nums[right]
				if quad_sum == target:
					quads.append([nums[i],nums[j],nums[left],nums[right]])
					left += 1
					right -= 1

					while left < right and nums[left] == nums[left - 1]:
						left += 1

					while left < right and nums[right] == nums[right + 1]:
						right -= 1
				elif quad_sum > target:
					right -= 1
				else:
					left += 1

	return quads



print(quadruple_sum_to_target([4, 1, 2, -1, 1, -3],1))
print(quadruple_sum_to_target([2, 0, -1, 1, -2, 2],2))




