import UIKit

var greeting = "Hello, playground"

// Pair with Target Sum

/*
 
 Given an array of sorted numbers and a target sum, find a pair
 in the array whose sum is equal to the given target

 Write a function to return the indices of the two numbers such that they
 add up to the given target

 Input: [1, 2, 3, 4, 6], target=6
 Output: [1, 3]
 Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

 Input: [2, 5, 9, 11], target=11
 Output: [0, 2]
 Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
 */

func twoSum(nums: [Int], target: Int) -> [Int] {
    
    var left = 0
    var right = nums.count - 1
    
    while left < right {
        let pairSum = nums[left] + nums[right]
        if pairSum > target {
            right -= 1
        } else if pairSum < target {
            left += 1
        } else {
            return [left, right]
        }
    }
    
    
    return []
}

twoSum(nums: [1, 2, 3, 4, 6], target: 6)
twoSum(nums: [2, 5, 9, 11], target: 11)

