# Permutation In A String

"""
Problem Statement

Given a string and a pattern, find out if the string 
contains any permutation of the pattern

Permutation is defined as the re-arranging of the characters
of the string. For example, "abc" had the following 
six permutations.

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.


Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""

def permutation_in_a_string(str, pattern):

	pattern_frequency = {}
	string_frequency = {}
	window_start = 0

	for char in pattern:
		if char in pattern_frequency:
			pattern_frequency[char] += 1
		else:
			pattern_frequency[char] = 1

	for window_end in range(len(str)):
		right_char = str[window_end]

		if right_char in string_frequency:
			string_frequency[right_char] += 1
		else:
			string_frequency[right_char] = 1


		if window_end >= len(pattern) - 1:

			if string_frequency == pattern_frequency:
				return True 

			left_char = str[window_start]

			string_frequency[left_char] -= 1

			if string_frequency[left_char] == 0:
				string_frequency.pop(left_char)

			window_start += 1

	return False

print(permutation_in_a_string("oidbcaf", "abc")) # True
print(permutation_in_a_string("odicf", "dc")) # False
print(permutation_in_a_string("bcdxabcdy", "bcdyabcdx")) # True
print(permutation_in_a_string("aaacb", "abc")) # True











