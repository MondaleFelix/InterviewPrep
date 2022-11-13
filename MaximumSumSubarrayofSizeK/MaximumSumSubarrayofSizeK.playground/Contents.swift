import UIKit

// Maximum Sum Subarray of Size K

/*
 Problem Statement

 Given an array of positive numbers and a positive number
 'k', find the maximum sum of an contiguous subarray of size 'k'

 Input: [2, 1, 5, 1, 3, 2], k=3
 Output: 9
 Explanation: Subarray with maximum sum is [5, 1, 3].

 Input: [2, 3, 4, 1, 5], k=2
 Output: 7
 Explanation: Subarray with maximum sum is [3, 4].

 */

func maxSumSubarrayofSizeK(nums: [Int], k: Int) -> Int {
    
    var maxSum = 0
    var windowSum = 0
    var windowStart = 0
    
    for windowEnd in 0 ..< nums.count {
        windowSum += nums[windowEnd]
        
        if windowEnd >= k - 1 {
            maxSum = max(maxSum,windowSum)
            windowSum -= nums[windowStart]
            windowStart += 1
        }
    }
    
    return maxSum
}

maxSumSubarrayofSizeK(nums: [2, 1, 5, 1, 3, 2], k: 3)
maxSumSubarrayofSizeK(nums: [2, 3, 4, 1, 5], k: 2)
