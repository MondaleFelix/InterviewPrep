import UIKit

// Valid Palindrome

/*
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
  
 */


func validPalindrome(str:String) -> Bool {
    
    var newString = Array(str.replacingOccurrences( of: "[^a-zA-Z0-9]", with: "", options: .regularExpression).lowercased())
    
    
    
    if newString.count == 0 {
        return true
    }
    
    var left = 0
    var right = newString.count - 1
    
    
    while left <= right {
        if newString[left] == newString[right] {
            left += 1
            right -= 1
        } else {
            return false
        }
    }
    
    return true

}

validPalindrome(str: "A man, a plan, a canal: Panama")
validPalindrome(str: "race a car")
validPalindrome(str: " ")

