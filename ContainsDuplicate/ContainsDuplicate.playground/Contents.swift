"""
Problem Statement

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct

Example 1:

Input: nums= [1, 2, 3, 4]
Output: false
Explanation: There are no duplicates in the given array.

Example 2:

Input: nums= [1, 2, 3, 1]
Output: true
Explanation: '1' is repeating.

"""

func containsDuplicate(nums:[Int]) -> Bool {
    
    var seen : [Int:Bool] = [:]
    
    for number in nums {
        if seen[number] == true {
            return true
        }
        seen[number] = true
    }
    
    return false
}

containsDuplicate(nums: [1, 2, 3, 4]) // false
containsDuplicate(nums: [1, 2, 3, 1]) // true
