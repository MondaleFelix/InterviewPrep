import UIKit

/*

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

 */


func reverseVowels(str: String) -> String{
    
    var str = Array(str)
    
    var left = 0
    var right = str.count - 1
    
    let vowels = "aeiouAEIOU"
        
    while right > left {
        
        while !vowels.contains(str[left]) {
            left += 1
        }
        
        while !vowels.contains(str[right]) {
            right -= 1
        }
        
        if right > left {
            str.swapAt(left, right)
            right -= 1
            left += 1
            
        }
        

        
    }

    
    
    return String(str)
}


reverseVowels(str: "hello")

reverseVowels(str: "AEIOU")

reverseVowels(str: "DesignGUrus")


