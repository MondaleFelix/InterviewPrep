import UIKit

// Squaring a Sorted Array

/*
 
 Given a sorted array, create a new array containing
 squares of all the numbers of the input array in the
 sorted order.

 Input: [-2, -1, 0, 2, 3]
 Output: [0, 1, 4, 4, 9]

 Input: [-3, -1, 0, 1, 2]
 Output: [0, 1, 1, 4, 9]

 */

func squaringASortedArray(nums: [Int]) -> [Int] {
    
    var left = 0
    var right = nums.count - 1
    var sortedArray: [Int] = []
    
    while left <= right {
        var leftSquared = nums[left] * nums[left]
        var rightSquared = nums[right] * nums[right]
        
        if rightSquared > leftSquared {
            sortedArray.append(rightSquared)
            right -= 1
        } else {
            sortedArray.append(leftSquared)
            left += 1
        }
    }
    
    return sortedArray.reversed()

}

squaringASortedArray(nums: [-2, -1, 0, 2, 3])
squaringASortedArray(nums: [-3, -1, 0, 1, 2])
