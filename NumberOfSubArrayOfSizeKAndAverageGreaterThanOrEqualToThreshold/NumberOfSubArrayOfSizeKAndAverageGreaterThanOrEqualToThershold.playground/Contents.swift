import UIKit

// Number of Subarray of Size K and Averagve Greater Than or Equal to Threshold

/*
 Problem Statement
 
 Given an array of integers arr and two integers K and Threshold,
 return the number of sub-arrays of size k and average greater than or equal
 to threshold

 Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
 Output: 3
 Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

 Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
 Output: 6
 Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

 */

func numberOfSubarrayOfSizeKAndAverageGreaterThanOrEqualToThreshold(arr: [Int], k: Int, threshold: Int)-> Int {
    
    var windowStart = 0
    var windowSum = 0
    var subarrayCount = 0
    
    for windowEnd in 0 ..< arr.count {
        windowSum += arr[windowEnd]
        
        if windowEnd >= k - 1 {
            let average = windowSum / k
            
            if average >= threshold {
                subarrayCount += 1
            }
            
            windowSum -= arr[windowStart]
            windowStart += 1
        }
    }
    return subarrayCount
}

numberOfSubarrayOfSizeKAndAverageGreaterThanOrEqualToThreshold(arr: [2,2,2,2,5,5,5,8], k: 3, threshold: 4)
numberOfSubarrayOfSizeKAndAverageGreaterThanOrEqualToThreshold(arr: [11,13,17,23,29,31,7,5,2,3], k: 3, threshold: 5)
