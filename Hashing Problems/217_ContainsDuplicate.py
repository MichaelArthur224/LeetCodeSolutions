'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a Hash Map to store items from num
        arr = {}
        # For every item in nums repeat
        for num in nums:
            # If the item is not in the hash map
            if num not in arr:
                # Add to hash map with Number as key and True as value (Ex. '1: True')
                # In this scenario imagine True = seen
                arr[num] = True
            # If item is in hash map then it is a duplicate so return True
            else:
                return True
        # Return False if no duplicates found
        return False
    
# Time Complexity: O(N)
