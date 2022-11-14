import UIKit

// Longest Substring with K Distinct Characters

/*
 
 Problem Statement
 
 Given a string, find the length of the longest substring in it with
 no more than K distinct characters
 
 You can assume that K is less than or equal to the length of the given
 string
 
 Input: String="araaci", K=2
 Output: 4
 Explanation: The longest substring with no more than '2' distinct characters is "araa".
 
 Input: String="araaci", K=1
 Output: 2
 Explanation: The longest substring with no more than '1' distinct characters is "aa".
 
 
 Input: String="cbbebi", K=3
 Output: 5
 Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
 
 */

func longestSubstringWithKDistinctCharacters(str: String, K: Int) -> Int {
    
    var windowStart = 0
    var maxLength = 0
    var charDict : [Character: Int] = [:]
    
    let str = Array(str)
    
    for windowEnd in 0 ..< str.count {
        var rightChar = str[windowEnd]
        
        if charDict[rightChar] == nil{
            charDict[rightChar] = 1
        } else {
            charDict[rightChar]! += 1
        }
        
        while charDict.count > K {
            var leftChar = str[windowStart]
            
            charDict[leftChar]! -= 1
            if charDict[leftChar] == 0 {
                charDict.removeValue(forKey: leftChar)
            }
            
            windowStart += 1
        }
        
        maxLength = max(maxLength, windowEnd - windowStart + 1)
        
    }
    return maxLength
}


longestSubstringWithKDistinctCharacters(str: "araaci", K: 2)
longestSubstringWithKDistinctCharacters(str: "araaci", K: 1)
longestSubstringWithKDistinctCharacters(str: "cbbebi", K: 3)
