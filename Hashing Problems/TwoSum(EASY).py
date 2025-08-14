'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hash map
        arr = {}
        # get index and value
        for i, num in enumerate(nums):
            # find target number
            targetNum = target - num
            # search for target in hash map
            if targetNum in arr:
                # return index
                return [arr[targetNum], i]
            # add to hash map if not already in it
            arr[num] = i
        # return empty array if not found
        return []

# Time Complexity: O(N)
