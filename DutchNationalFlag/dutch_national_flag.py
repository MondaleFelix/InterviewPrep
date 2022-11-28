# Dutch National Flag

"""

Problem Statement

Given an array of containing 0s, 1s, 2s, sort the array
in-place. You should treat numbers of the array as objects,
hence,  we can't count 0s, 1s, and 2s to recreate the array

The flag of the Netherlands consists of three colors: red, white,
blue; and since our input array also consists of three different numbers
that is why it is called Dutch National Flag

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

"""

def dutch_national_flag(nums):

	low = 0
	high = len(nums) - 1

	i = 0

	while i <= high:
		if nums[i] == 0:
			nums[i], nums[low] = nums[low], nums[i]
			i += 1
			low += 1

		elif nums[i] == 1:
			i += 1
		else:
			nums[i], nums[high] = nums[high], nums[i]
			high -= 1

	return nums



print(dutch_national_flag([1, 0, 2, 1, 0]))
print(dutch_national_flag([2, 2, 0, 1, 2, 0]))
