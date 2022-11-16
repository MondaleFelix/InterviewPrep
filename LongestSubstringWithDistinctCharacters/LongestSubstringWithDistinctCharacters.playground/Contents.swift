import UIKit

// Longest Substring with Distinct Characters

/*
 
 Problem Statement
 
 Given a string, find the length of the longest substring,
 which has all distinct characters.
  
 Input: String="aabccbb"
 Output: 3
 Explanation: The longest substring with distinct characters is "abc".

 Input: String="abbbb"
 Output: 2
 Explanation: The longest substring with distinct characters is "ab".

 
 */

func longestSubstringWithDistinctCharacters(str: String) -> Int {
    
    var maxLength = 0
    var windowStart = 0
    var charIndex : [Character: Int] = [:]
    let str = Array(str)
    
    for windowEnd in 0 ..< str.count {
        
        var rightChar = str[windowEnd]
        
        if charIndex[rightChar] == nil {
            charIndex[rightChar] = windowEnd
        } else {
            charIndex[rightChar] = windowStart
            windowStart += 1
        }
        
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    }
    
    
    return maxLength
}

longestSubstringWithDistinctCharacters(str: "aabccbb")
longestSubstringWithDistinctCharacters(str: "abbbb")

