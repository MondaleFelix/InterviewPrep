# Fruits into Baskets

"""
Problem Statement

You are visiting a farm to collect fruits. 
The farm has a single row of fruit trees. 
You will be given two baskets, and your goal is to pick as many fruits 
as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. 
The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""

def fruits_into_baskets(fruits):

	fruit_basket = {}
	max_fruits = 0
	window_start = 0 

	for window_end in range(len(fruits)):
		right_fruit = fruits[window_end]

		if right_fruit in fruit_basket:
			fruit_basket[right_fruit] += 1
		else: 
			fruit_basket[right_fruit] = 1

		while len(fruit_basket) > 2:
			left_fruit = fruits[window_start]

			fruit_basket[left_fruit] -= 1

			if fruit_basket[left_fruit] == 0:
				fruit_basket.pop(left_fruit)

			window_start += 1

		max_fruits = max(max_fruits, window_end - window_start + 1)

	return max_fruits


print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))














