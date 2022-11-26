import UIKit

// Triplets With Smaller Sum

/*
 
 Problem Statement

 Given an array arr of unsorted numbers and a target sum,
 count all triplets in it such that
 arr[i] + arr[j] + arr[k] < target where i, j, and k are
 three different indices. Write a function to
 return the count of such triplets.

 Input: [-1, 0, 2, 3], target=3
 Output: 2
 Explanation: There are two triplets whose sum
 is less than the target: [-1, 0, 3], [-1, 0, 2]

 Input: [-1, 4, 2, 1, 3], target=5
 Output: 4
 Explanation: There are four triplets whose sum is
 less than the target:
    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
  
 */


func tripletsWithSmallerSum(nums: [Int], target: Int) -> Int {
    
    let nums = nums.sorted()
    var tripletCount = 0
    
    for i in 0 ..< nums.count - 2 {
        var left = i + 1
        var right = nums.count - 1
        
        while left <= right {
            var tripletSum = nums[i] + nums[left] + nums[right]
            
            if tripletSum > target {
                right -= 1
            } else {
                tripletCount += 1
                left += 1
            }
            
        }
    }
    return tripletCount
}

tripletsWithSmallerSum(nums: [-1, 0, 2, 3], target: 3)
tripletsWithSmallerSum(nums: [-1, 4, 2, 1, 3], target: 5)
