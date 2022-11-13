import UIKit

// Smallest Subarray with a Greater Sum

/*
 Problem Statement
 
 Given an array of positive numbers and a positive number 'S'
 Find the length of the smallest contigious subarray whose sum
 is greater than or equal to 'S'. Return 0 if no such subarray exists

 Input: [2, 1, 5, 2, 3, 2], S=7
 Output: 2
 Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

 Input: [2, 1, 5, 2, 8], S=7
 Output: 1
 Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

 Input: [3, 4, 1, 1, 6], S=8
 Output: 3
 Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1]
 or [1, 1, 6].
  
 */

func smallestSubarrayWithGreaterSum(nums: [Int], s: Int) -> Int {
    
    var minLength = nums.count + 1
    var windowSum = 0
    var windowStart = 0
    
    for windowEnd in 0 ..< nums.count {
        windowSum += nums[windowEnd]
        
        while windowSum >= s {
            minLength = min(minLength, windowEnd - windowStart + 1)
            windowSum -= nums[windowStart]
            windowStart += 1
        }
    }
    
    if minLength == nums.count + 1 {
        return 0
    }
    
    return minLength
    
}

smallestSubarrayWithGreaterSum(nums: [2, 1, 5, 2, 3, 2], s: 7)
smallestSubarrayWithGreaterSum(nums: [2, 1, 5, 2, 8], s: 7)
smallestSubarrayWithGreaterSum(nums: [3, 4, 1, 1, 6], s: 8)
