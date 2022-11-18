# Smallest Window Containing Substring

"""
Problem Statement

Given a string, find the smallest substring in the given string
which has all the character occurrences of the given string\

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Input: String="aabdec", Pattern="abac"
Output: "aabdec"
Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern

"""

def smallest_window_containing_substring(str, pattern):

	window_start = 0
	min_length = len(str) + 1
	pattern_frequency = {}
	string_frequency = {}
	matched_count = 0
	substring = ""

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

		if right_char in pattern_frequency and string_frequency[right_char] <= pattern_frequency[right_char]:
				matched_count += 1

		# print(matched_count)
		while matched_count == len(pattern):

			min_length = min(min_length, window_end - window_start + 1)

			substring = str[window_start:window_end+1]
			# print(substring)


			left_char = str[window_start]

			string_frequency[left_char] -= 1

			if left_char in pattern_frequency and string_frequency[left_char] < pattern_frequency[left_char]:
				matched_count -= 1

			if string_frequency[left_char] == 0:
				string_frequency.pop(left_char)

			window_start += 1 

	if min_length == len(str) + 1:
		return ""

	return substring

print(smallest_window_containing_substring("aabdec","abc")) #5
print(smallest_window_containing_substring("aabdec","abac")) #6
print(smallest_window_containing_substring("abdbca","abc"))#3
print(smallest_window_containing_substring("adcad","abc")) #0











