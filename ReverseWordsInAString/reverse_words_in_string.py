# Reverse Words In A String

"""
Problem Statement

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated
by a single space.

Note that s may contain leading or trailing spaces or 
multiple spaces between two words. The returned string 
should only have a single space separating the words. 
Do not include any extra spaces.


Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or
trailing spaces.


Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between
two words to a single space in the reversed string.
"""

def reverse_words_in_string(str):

	str = str.split(" ")
	str = [x for x in str if x]

	left = 0
	right = len(str) - 1


	while left < right:

		str[left], str[right] = str[right], str[left]
		left += 1
		right -= 1

	return " ".join(str)

print(reverse_words_in_string("the sky is blue"))
print(reverse_words_in_string("  hello world  "))
print(reverse_words_in_string("a good   example"))
