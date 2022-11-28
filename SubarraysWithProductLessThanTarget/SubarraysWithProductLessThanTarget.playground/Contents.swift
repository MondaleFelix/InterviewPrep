import UIKit

// Subarrays With Product Less Than a Target

/*
 
 Problem Statement

 Given an array with positive numbers and a postive target
 number, find all of its contiguous subarrays whose product
 is less than the target number

 Input: [2, 5, 3, 10], target=30
 Output: [2], [5], [2, 5], [3], [5, 3], [10] ->6
 Explanation: There are six contiguous subarrays whose product is less than the target.

 Input: [8, 2, 6, 5], target=50
 Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]  -> 7
 Explanation: There are seven contiguous subarrays whose product is less than the target.
 
 */




func subarraysWithProductLessThanTarget(nums: [Int], target: Int) -> Int {
    
    var windowEnd = 0
    var product = 1
    var count = 0
//    var subarrays : [[Int]] = []
    
    for windowStart in 0 ..< nums.count {
        windowEnd = windowStart
        product *= nums[windowEnd]
        
        while product < target {
            count += 1
//            subarrays.append(nums[windowStart...windowEnd])

            if windowEnd == nums.count - 1 {
                break
            }
            windowEnd += 1
            product *= nums[windowEnd]
            
        }
        
        product = 1
    }
    
    return count
}


subarraysWithProductLessThanTarget(nums: [2, 5, 3, 10], target: 30)
subarraysWithProductLessThanTarget(nums: [8, 2, 6, 5], target: 50)
