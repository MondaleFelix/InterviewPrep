# Longest Substring with Distinct Characters

"""
Problem Statement

Given a string, find the length of the longest substring,
which has all distinct characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".


"""

def longest_substring_with_distinct_characters(str):

	max_length = 0
	window_start = 0
	char_index = {}

	for window_end in range(len(str)):

		right_char = str[window_end]

		if right_char in char_index:
			char_index[right_char] = window_start
			window_start += 1
		else:
			char_index[right_char] = window_end

		max_length = max(max_length, window_end - window_start + 1)


	return max_length


print(longest_substring_with_distinct_characters("aabccbb"))
print(longest_substring_with_distinct_characters("abbbb"))






