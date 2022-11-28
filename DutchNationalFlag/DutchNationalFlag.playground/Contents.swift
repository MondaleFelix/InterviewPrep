import UIKit

// Dutch National Flag

/*
 
 Problem Statement

 Given an array of containing 0s, 1s, 2s, sort the array
 in-place. You should treat numbers of the array as objects,
 hence,  we can't count 0s, 1s, and 2s to recreate the array

 The flag of the Netherlands consists of three colors: red, white,
 blue; and since our input array also consists of three different numbers
 that is why it is called Dutch National Flag

 Input: [1, 0, 2, 1, 0]
 Output: [0 0 1 1 2]

 Input: [2, 2, 0, 1, 2, 0]
 Output: [0 0 1 2 2 2 ]
 

 */

func dutchNationalFlag(nums:[Int]) -> [Int] {
    
    var low = 0
    var high = nums.count - 1
    
    var nums = nums
    
    var i = 0
    
    while i <= high {
        if nums[i] == 0 {
            nums.swapAt(i, low)
            low += 1
            i += 1
        } else if nums[i] == 1 {
            i += 1
        } else {
            nums.swapAt(i, high)
            high -= 1
        }
    }
    
    return nums
}

dutchNationalFlag(nums: [1, 0, 2, 1, 0])
dutchNationalFlag(nums: [2, 2, 0, 1, 2, 0])
