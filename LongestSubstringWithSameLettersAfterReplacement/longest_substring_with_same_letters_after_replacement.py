# Longest Substring with Same Letters after Replacement

"""
Problem Statement

Given a string with lowercase letters only, if you are allowed
to replace no more than ‘k’ letters with any letter, find the
length of the longest substring having the same letters
after replacement

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""



def longest_substring_with_same_letters_after_replacement(str, k):

	max_replacement_count = 0
	max_length = 0
	window_start = 0
	char_frequency = {}

	for window_end in range(len(str)):
		right_char = str[window_end]

		if right_char in char_frequency:
			char_frequency[right_char] += 1
		else:
			char_frequency[right_char] = 1

		max_replacement_count = max(max_replacement_count, char_frequency[right_char])


		while (window_end - window_start + 1) - max_replacement_count > k:
			window_start += 1

		max_length = max(max_length, window_end - window_start + 1)


	return max_length

print(longest_substring_with_same_letters_after_replacement("aabccbb",2))
print(longest_substring_with_same_letters_after_replacement("abbcb",1))
print(longest_substring_with_same_letters_after_replacement("abccde",1))


