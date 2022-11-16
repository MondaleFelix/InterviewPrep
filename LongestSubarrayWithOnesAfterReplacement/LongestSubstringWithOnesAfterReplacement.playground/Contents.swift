import UIKit

// Longest Substring with Ones after Replacement

/*
 
 Problem Statement

 Given an array containing 0s and 1s, if you are allowed to
 replace no more than ‘k’ 0s with 1s, find the length of the
 longest contiguous subarray having all 1s.

 Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
 Output: 6
 Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

 Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
 Output: 9
 Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
 
 
 */

func longestSubstringWithOnesAfterReplacement(nums: [Int], k: Int) -> Int {
    
    var windowStart = 0
    var maxLength = 0
    var zeroCount = 0
    
    for windowEnd in 0 ..< nums.count {
        var rightNum = nums[windowEnd]
        
        if rightNum == 0 {
            zeroCount += 1
        }
        
        while zeroCount > k {
            var leftNumber = nums[windowStart]
            if leftNumber == 0 {
                zeroCount -= 1
            }
            windowStart += 1
        }
        
        maxLength = max(maxLength, windowEnd - windowStart + 1)
    }
    
    return maxLength
}


longestSubstringWithOnesAfterReplacement(nums: [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k: 2)
longestSubstringWithOnesAfterReplacement(nums: [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k: 3)
