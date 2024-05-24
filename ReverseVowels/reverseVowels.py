"""

Problem Statement

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s= "hello"
Output: "holle"
Example 2:

Input: s= "AEIOU"
Output: "UOIEA"
Example 3:

Input: s= "DesignGUrus"
Output: "DusUgnGires"


"""

def reverseVowels(string):

	string = list(string)

	l = 0
	r = len(string) - 1

	vowels = "aeiouAEIOU"


	while l < r:
		while string[l] not in vowels:
			l += 1

		while string[r] not in vowels:
			r -= 1

		string[l],string[r] = string[r], string[l]


		l += 1
		r -= 1

		if r > l:
			break

	return "".join(string)





print(reverseVowels("hello"))
print(reverseVowels("AEIOU"))
print(reverseVowels("DesignGUrus"))
