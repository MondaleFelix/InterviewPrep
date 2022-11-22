import UIKit

// Triplet Sum Close to Target

/*
 
 Problem Statement
 
 Given an array of unsorted numbers and a target number, find a triplet in the array
 whose sum is as close to target number as possible, return the sum of the triplet.
 If there are more than such triplet, return the sum of the triplet with the smallest
 sum
 
 Input: [-2, 0, 1, 2], target=2
 Output: 1
 Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
 
 Input: [-3, -1, 1, 2], target=1
 Output: 0
 Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
 
 Input: [1, 0, 1, 1], target=100
 Output: 3
 Explanation: The triplet [1, 1, 1] has the closest sum to the target.
 
 Input: [0, 0, 1, 1, 2, 6], target=5
 Output: 4
 Explanation: There are two triplets with distance '1' from target: [1, 1, 2] & [0,0, 6]. Between these two triplets, the correct answer will be [1, 1, 2] as it has a sum '4' which is less than the sum of the other triplet which is '6'. This is because of the following requirement: 'If there are more than one such triplet, return the sum of the triplet with the smallest sum.'
 */

func tripletSumCloseToTarget(nums:[Int], target: Int) -> Int {
    
    let nums = nums.sorted()
    var minDistance = target
    
    for i in 0 ..< nums.count - 2 {
        var left = i + 1
        var right = nums.count - 1
        
        
        while left < right {
            var tripletSum = nums[i] + nums[left] + nums[right]
            
            if tripletSum > target {
                minDistance = min(minDistance, tripletSum - target)
                right -= 1
            } else {
                minDistance = min(minDistance, target - tripletSum)
                left += 1
            }
        }
    }
    
    return target - minDistance
}

tripletSumCloseToTarget(nums: [-2, 0, 1, 2], target: 2)
tripletSumCloseToTarget(nums: [-3, -1, 1, 2], target: 1)
tripletSumCloseToTarget(nums: [1, 0, 1, 1], target: 100)
tripletSumCloseToTarget(nums: [0, 0, 1, 1, 2, 6], target: 5)
