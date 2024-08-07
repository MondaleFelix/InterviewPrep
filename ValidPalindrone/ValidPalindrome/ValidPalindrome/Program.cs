using System;
using System.Text;

namespace ValidPalindrome;

/*
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Input: sentence = "A man, a plan, a canal, Panama!"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Input: sentence = "Was it a car or a cat I saw?"
Output: true
Explanation: Explanation: "wasitacaroracatisaw" is a palindrome.
 */


class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        bool test1 = ValidPalindrome("A man, a plan, a canal, Panama!");
        bool test2 = ValidPalindrome("Was it a car or a cat I saw?");
        bool test3 = ValidPalindrome("Hello World");

        Console.WriteLine(test1);
        Console.WriteLine(test2);
        Console.WriteLine(test3);
        Console.ReadKey();

    }

    //TODO: 

    static bool ValidPalindrome(string sentence)
    {

        sentence = CleanString(sentence);

        int left = 0;
        int right = sentence.Length - 1;

        while (right > left)
        {
            char leftChar = sentence[left];
            char rightChar = sentence[right];

            if (leftChar == rightChar)
            {
                right -= 1;
                left += 1;
            } else
            {
                return false;
            }

        }

        return true;
    }


    //TODO: Clean input string to only contain letters and numbers

    static string CleanString(string str)
    {

        List<char> charList = new List<char>();


        foreach(char letter in str)
        {
            if (char.IsLetterOrDigit(letter)){
                charList.Add(letter);
            }

        }

        string cleanedString = string.Join("", charList);
        return cleanedString.ToLower();
    }







}

