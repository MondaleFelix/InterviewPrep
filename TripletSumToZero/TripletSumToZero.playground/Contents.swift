import UIKit

// Triplet Sum to Zero

/*
 
 Given an array of unsorted numbers, find all unique triplets in it
 that add up to zero
 
 Input: [-3, 0, 1, 2, -1, 1, -2]
 Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
 Explanation: There are four unique triplets whose sum is equal to zero.
 
 Input: [-5, 2, -1, -2, 3]
 Output: [[-5, 2, 3], [-2, -1, 3]]
 Explanation: There are two unique triplets whose sum is equal to zero.

 */

func tripletsSumToZero(nums: [Int]) -> [[Int]] {
    
    let nums = nums.sorted()
    var triplets: [[Int]] = []
    
    for i in 0 ..< nums.count - 2 {
        
        var left = i + 1
        var right = nums.count - 1
        
        if i > 0  && nums[i] == nums[i-1] {
            continue
        }
        
        
        while left < right {
            var tripletsSum = nums[i] + nums[left] + nums[right]
            
            if tripletsSum == 0 {
                triplets.append([nums[i], nums[left], nums[right]])
                
                right -= 1
                left += 1
                
                while nums[left] == nums[left - 1] {
                    left += 1
                }
                
                while nums[right] == nums[right + 1] {
                    right += 1
                }
                
                
            } else if tripletsSum > 0 {
                right -= 1
            } else {
                left += 1
            }
            
            
        }
        
    }
    
    return triplets
}


tripletsSumToZero(nums: [-3, 0, 1, 2, -1, 1, -2])
tripletsSumToZero(nums: [-5, 2, -1, -2, 3])

