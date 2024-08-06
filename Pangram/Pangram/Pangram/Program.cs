namespace Pangram;

/*

Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or false otherwise.

Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

Example 1:

Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
Output: true
Explanation: The sentence contains at least one occurrence of every letter of the English alphabet either in lower or upper case.

Example 2:

Input: sentence = "This is not a pangram"
Output: false
Explanation: The sentence doesn't contain at least one occurrence of every letter of the English alphabet.

 */


class Program
{
    static void Main(string[] args)
    {
        bool test1 = isPangram("TheQuickBrownFoxJumpsOverTheLazyDog");
        bool test2 = isPangram("This is not a pangram");

        Console.WriteLine(test1);
        Console.WriteLine(test2);
        Console.ReadKey();
    }

    static bool isPangram(string sentence)
    {
        sentence = cleanString(sentence);
        string alphabet = "abcdefghijklmnopqrstuvwxyz";

        Dictionary<char, bool> seen = new Dictionary<char, bool>();
      

        foreach (char letter in sentence)
        {
            if (alphabet.Contains(letter) && !seen.ContainsKey(letter))
            {
                seen[letter] = true;
            }
        }

        if (alphabet.Length == seen.Count) {
            return true;
        } else
        {
            return false;
        }

    }



    static string cleanString(string str)
    {
        string cleanedString = str.Replace(" ", "").ToLower();
        return cleanedString;
    }

}

