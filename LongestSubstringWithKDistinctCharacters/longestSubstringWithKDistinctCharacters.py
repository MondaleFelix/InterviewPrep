# Longest Substring with K Distinct Characters

'''
Problem Statement

Given a string, find the length of the longest substring in it
with no more than k distinct characters

You can assume that K is less than or equal to the length of the given string.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".


Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

'''

def longest_substring_with_distinct_characters(str, K):

	char_dict = {}
	window_start = 0
	max_length = 0

	for window_end in range(len(str)):

		right_char = str[window_end]

		if right_char in char_dict:
			char_dict[right_char] += 1
		else:
			char_dict[right_char] = 1

		while len(char_dict) > K:

			left_char = str[window_start]
			char_dict[left_char] -= 1

			if char_dict[left_char] == 0:
				char_dict.pop(left_char)

			window_start += 1

		max_length = max(max_length, window_end - window_start + 1)

	return max_length

 
print(longest_substring_with_distinct_characters("araaci", 2)) #4
print(longest_substring_with_distinct_characters("araaci", 1)) #2
print(longest_substring_with_distinct_characters("cbbebi", 3)) #5

