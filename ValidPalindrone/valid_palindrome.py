# Valid Palindrome

"""
A phrase is a palinfrome if, after converting all uppercase letters into lowercase and
removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

import re

def valid_palindrome(str):

	s = ''.join(c for c in str if c.isalnum()).lower()

	if len(s) == 0:
		return True


	left = 0
	right = len(s) - 1

	while left <= right:
		if s[left] == s[right]:
			left += 1
			right -= 1
		else:
			return False

	return True




print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))
print(valid_palindrome(" "))
