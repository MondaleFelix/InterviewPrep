import UIKit

// Permutation In a String

/*
 
 Problem Statement

 Given a string and a pattern, find out if the string
 contains any permutation of the pattern

 Permutation is defined as the re-arranging of the characters
 of the string. For example, "abc" had the following
 six permutations.

 1. abc
 2. acb
 3. bac
 4. bca
 5. cab
 6. cba

 Input: String="oidbcaf", Pattern="abc"
 Output: true
 Explanation: The string contains "bca" which is a permutation of the given pattern

 Input: String="odicf", Pattern="dc"
 Output: false
 Explanation: No permutation of the pattern is present in the given string as a substring.

 Input: String="bcdxabcdy", Pattern="bcdyabcdx"
 Output: true
 Explanation: Both the string and the pattern are a permutation of each other.


 Input: String="aaacb", Pattern="abc"
 Output: true
 Explanation: The string contains "acb" which is a permutation of the given pattern.
 
 */

func permutationInAString(str: String, pattern:String) -> Bool {
    
    var stringFrequency: [Character: Int] = [:]
    var patternFrequency: [Character: Int] = [:]
    var windowStart = 0
    let str = Array(str)
    for char in pattern {
        if patternFrequency[char] == nil {
            patternFrequency[char] = 1
        } else {
            patternFrequency[char]! += 1
        }
    }
    
    for windowEnd in 0 ..< str.count {
        var rightChar = str[windowEnd]
        
        if stringFrequency[rightChar] == nil {
            stringFrequency[rightChar] = 1
        } else {
            stringFrequency[rightChar]! += 1
        }
        
        if windowEnd >= pattern.count - 1 {
            
            if stringFrequency == patternFrequency {
                return true
            }
            
            var leftChar = str[windowStart]
            
            stringFrequency[leftChar]! -= 1
            
            if stringFrequency[leftChar] == 0 {
                stringFrequency.removeValue(forKey: leftChar)
            }
            windowStart += 1
        }
    }
    return false
}

permutationInAString(str: "oidbcaf", pattern: "abc")
permutationInAString(str: "odicf", pattern: "dc")
permutationInAString(str: "bcdxabcdy", pattern: "bcdyabcdx")
permutationInAString(str: "aaacb", pattern: "abc")
