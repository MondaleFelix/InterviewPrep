import UIKit

// String Anagrams


/*
 
 Problem Statement

 Given a string and a pattern, find all anagrams of the pattern
 in the given string

 Every anagram is a permutation of a string. As we know, when we
 are not allowe to repeat characters while finding permutation
 of a string, we get N! permutation (or anagrams) of a string
 hacing N characters. For example, here are the size anagrams
 of the string "abc"

 1. abc
 2. acb
 3. bac
 4. bca
 5. cab
 6. cba

 Input: String="ppqp", Pattern="pq"
 Output: [1, 2]
 Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

 Input: String="abbcabc", Pattern="abc"
 Output: [2, 3, 4]
 Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
 */

func stringAnagrams(str: String, pattern: String) -> [Int] {
    
    var stringFrequency: [Character: Int] = [:]
    var patternFrequency: [Character: Int] = [:]
    var windowStart = 0
    var permutationIndex: [Int] = []
    
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
                permutationIndex.append(windowStart)
            }
            
            var leftChar = str[windowStart]
            
            stringFrequency[leftChar]! -= 1
            if stringFrequency[leftChar] == 0 {
                stringFrequency.removeValue(forKey: leftChar)
            }
            windowStart += 1
        }
    }
    
    return permutationIndex
}

print(stringAnagrams(str: "ppqp", pattern: "pq"))
print(stringAnagrams(str: "abbcabc", pattern: "abc"))
