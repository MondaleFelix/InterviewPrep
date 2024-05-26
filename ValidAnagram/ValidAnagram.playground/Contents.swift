import UIKit

var greeting = "Hello, playground"

/*
  
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
 
 */

func validAnagram(str1: String, str2: String) -> Bool {
    
    var str1_frequency: [Character: Int] = [:]
    var str2_frequency: [Character: Int] = [:]
    
    for letter in str1 {
        if str1_frequency[letter] == nil {
            str1_frequency[letter] = 0
        } else {
            str1_frequency[letter]! += 1
        }
    }
    
    for letter in str2 {
        if str2_frequency[letter] == nil {
            str2_frequency[letter] = 0
        } else {
            str2_frequency[letter]! += 1
        }
    }
    
    return str1_frequency == str2_frequency
    
}

validAnagram(str1: "listen", str2: "silent")
validAnagram(str1: "rat", str2: "car")
validAnagram(str1: "hello", str2: "world")



