# Triplet Sum Close to Target

"""
Problem Statement

Given an array of unsorted numbers and a target number, find
a triplet in the array whose sum is as close to the target
as possible, return the sum of the triplet. If there are more
than one such triplet, return sum of the sum of the triplet
with the smallest sum

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.


Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

Input: [0, 0, 1, 1, 2, 6], target=5
Output: 4

Explanation: There are two triplets with distance '1' from target: [1, 1, 2] & [0,0, 6].
Between these two triplets, the correct answer will be [1, 1, 2] as it has a sum '4'
which is less than the sum of the other triplet which is '6'. This is because of the 
following requirement: 'If there are more than one such triplet, 
return the sum of the triplet with the smallest sum.'
"""

# Sort the numbers array
# Keep track of minimum value to target
# Iterate through the array
	# establish left pointer
	# establish right pointer

	# Handle duplicate values

	# Calculate sum of three pointers

		# if sum is greater than target 
			#  min value =  triplet sum - target
		# else target is greater than triplet sum
		#  min value = target - triplet sum


# return min value

def triplet_sum_close_to_target(nums, target): 

	nums.sort()
	min_distance = target

	for i in range(len(nums) - 2) :
		left = i + 1
		right = len(nums) - 1 

		if nums[i] == nums[i - 1]: 
			continue

		while left < right: 
			triplets_sum = nums[i] + nums[left] + nums[right]

			if triplets_sum > target: 
				min_distance = min(min_distance, triplets_sum - target)
				right -= 1
			else:
				min_distance = min(min_distance, target - triplets_sum)
				left += 1

	return target - min_distance

print(triplet_sum_close_to_target([-2, 0, 1, 2],2))
print(triplet_sum_close_to_target([-3, -1, 1, 2],1))
print(triplet_sum_close_to_target([1, 0, 1, 1],100))
print(triplet_sum_close_to_target([0, 0, 1, 1, 2, 6],5))












