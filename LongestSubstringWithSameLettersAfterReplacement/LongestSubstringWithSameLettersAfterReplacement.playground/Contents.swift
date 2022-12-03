import UIKit

// Longest Substring With Same Letters After Replacement

/*
 
 Problem Statement
 
 Given an string with lowercase letters only, if you are
 allowed to replace no more than 'k' letters with any letter,
 find the length of the longest substring having the same
 letters after replacement
 
 Input: String="aabccbb", k=2
 Output: 5
 Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
 
 Input: String="abbcb", k=1
 Output: 4
 Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
 
 Input: String="abccde", k=1
 Output: 3
 Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
 
 
 */

/*
 
 Iterate through the string
 Store count of each letter
 Keep track of max occurance of any letter
 
 If window - max occureance > k
 Move left side of the window
 
 */

func longestSubstringWithSameLettersAfterReplacement(str: String, k: Int) -> Int {
    
    var str = Array(str)
    var windowStart = 0
    
    var charCount: [Character: Int] = [:]
    var maxCharCount = 0
    var longestSubstring = 0
    
    for windowEnd in 0 ..< str.count {
        var rightChar = str[windowEnd]
        
        if charCount[rightChar] == nil {
            charCount[rightChar] = 1
        } else {
            charCount[rightChar]! += 1
        }
        
        maxCharCount = max(maxCharCount, charCount[rightChar]!)
        
        while windowEnd - windowStart + 1 - maxCharCount > k {
            windowStart += 1
            
        }
        
        longestSubstring = max(longestSubstring, windowEnd - windowStart + 1)

    }
    
    
    
    return longestSubstring
    
    
    
}

longestSubstringWithSameLettersAfterReplacement(str: "aabccbb", k: 2)
longestSubstringWithSameLettersAfterReplacement(str: "abbcb", k: 1)
longestSubstringWithSameLettersAfterReplacement(str: "abccde", k: 1)


