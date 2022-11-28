import UIKit

// Quadruple Sum To Target

/*
 
 Problem Statement
 
 Given an array od unsorted numbers and a target number, find
 all unique quadruplets in it, whose sum is equal to the target
 number

 Input: [4, 1, 2, -1, 1, -3], target=1
        [-3, -1, 1, 1, 2, 4]


 Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
 Explanation: Both the quadruplets add up to the target.

 Input: [2, 0, -1, 1, -2, 2], target=2
 Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
 Explanation: Both the quadruplets add up to the target.
 
 */

func quadrupleSumToTarget(nums:[Int], target: Int) -> [[Int]] {
    
    let nums = nums.sorted()
    var quads: [[Int]] = []
    
    for i in 0 ..< nums.count - 3 {
        if i > 0 && nums[i] == nums[i - 1] {
            continue
        }
        
        for j in i+1 ..< nums.count - 2 {
            if j > i + 1 && nums[j] == nums[j - 1] {
                continue
            }

            var left = j + 1
            var right = nums.count - 1
            
            while left < right {
                var quadSum = nums[i] + nums[j] + nums[left] + nums[right]
                
                if quadSum == target {
                    quads.append(contentsOf: [[nums[i],nums[j],nums[left],nums[right]]])
                    left += 1
                    right -= 1
                    
                    while left < right && nums[left] == nums[left - 1] {
                        left += 1
                    }
                    
                    while left < right && nums[right] == nums[right + 1] {
                        right -= 1
                    }
                } else if quadSum > target {
                    right -= 1
                } else {
                    left += 1
                }
            }

        }
    }

    return quads
    
}

quadrupleSumToTarget(nums: [4, 1, 2, -1, 1, -3], target: 1)
quadrupleSumToTarget(nums: [2, 0, -1, 1, -2, 2], target: 2)
