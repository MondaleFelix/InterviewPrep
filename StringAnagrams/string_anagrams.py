# String Anagrams

"""
Problem Statement

Given a string and a pattern, find all anagrams of the pattern
in the given string

Every anagram is a permutation of a string. As we know, when we 
are not allowe to repeat characters while finding permutation
of a string, we get N! permutation (or anagrams) of a string
hacing N characters. For example, here are the size anagrams
of the string "abc"

1. abc
2. acb
3. bac
4. bca
5. cab
6. cba

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


"""

def string_anagrams(string, pattern): 

	string_frequency = {}
	pattern_frequency = {}
	window_start = 0
	permutations_index = []

	for char in pattern:
		if char in pattern_frequency:
			pattern_frequency[char] += 1
		else:
			pattern_frequency[char] = 1


	for window_end in range(len(string)):
		right_char = string[window_end]

		if right_char in string_frequency:
			string_frequency[right_char] += 1
		else:
			string_frequency[right_char] = 1

		if window_end >= len(pattern) - 1:

			if string_frequency == pattern_frequency:
				permutations_index.append(window_start)

			left_char = string[window_start]

			string_frequency[left_char] -= 1
			if string_frequency[left_char] == 0:
				string_frequency.pop(left_char)

			window_start += 1


	return permutations_index

print(string_anagrams("ppqp","pq"))
print(string_anagrams("abbcabc","abc"))














