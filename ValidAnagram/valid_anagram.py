"""

Valid Anagram (easy)

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input: s = "listen", t = "silent"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Example 3:

Input: s = "hello", t = "world"
Output: false

"""

def valid_anagram(str1,str2):

	str1_count = {}
	str2_count = {}

	for letter in str1:
		if letter in str1_count.keys():
			str1_count[letter] += 1
		else:
			str1_count[letter] = 1

	for letter in str2:
		if letter in str2_count.keys():
			str2_count[letter] += 1
		else:
			str2_count[letter] = 1

	return str1_count == str2_count


print(valid_anagram("listen", "silent")) #true
print(valid_anagram("car", "rat")) # false
print(valid_anagram("hello", "world")) #false