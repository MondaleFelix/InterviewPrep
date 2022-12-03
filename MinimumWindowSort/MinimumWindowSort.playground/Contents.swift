import UIKit

// Minimum Window Sort

/*
 
 Problem Statement
 Given an array, find the length of the smallest subarray in it
 which when sorted will sort the whole array.
 
 Input: [1, 2, 5, 3, 7, 10, 9, 12]
 Output: 5
 Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
 
 Input: [1, 3, 2, 0, -1, 7, 10]
 Output: 5
 Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
 
 Input: [1, 2, 3]
 Output: 0
 Explanation: The array is already sorted
 
 Input: [3, 2, 1]
 Output: 3
 Explanation: The whole array needs to be sorted.
 */


func minimumWindowSort(nums:[Int]) -> Int{
    
    var left = 0
    var right = nums.count - 1
    
    while nums[left] < nums[left + 1] && left < nums.count - 1 {
        left += 1
        
        if left == nums.count - 1 {
            return 0
        }
    }
    
    while nums[right - 1] < nums[right] && right > 0 {
        right -= 1


    }
    
    if right == nums.count - 1 {
        return nums.count
    }

    var minNumber = nums[left]
    var maxNumber = nums[right]


    for number in nums[left...right] {
        minNumber = min(minNumber, number)
        maxNumber = max(maxNumber, number)

    }


    print(left, right)

    while minNumber < nums[left - 1] && left > 0{
        left -= 1
        if left == 0 {
            break
        }
    }

    while maxNumber > nums[right + 1] && right < nums.count - 1 {
        right += 1

        if right == nums.count  - 1 {
            break
        }

    }
    
    return right - left + 1
}

minimumWindowSort(nums: [1, 2, 5, 3, 7, 10, 9, 12])
minimumWindowSort(nums: [1, 3, 2, 0, -1, 7, 10])
minimumWindowSort(nums: [1, 2, 3])
minimumWindowSort(nums: [3, 2, 1])
