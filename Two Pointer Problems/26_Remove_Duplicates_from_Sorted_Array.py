'''Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such 
that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums. '''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # pointer starting at 0 index
        slow = 0
        # pointer starting at 1 index
        fast = 1
        # fast will move by 1 for the length of nums
        for fast in range(1,len(nums)):
            # if index values do not match
            if nums[slow] != nums[fast]:
                # move slow pointer forward to make space for a new unique element
                slow += 1
                # copy the unique element at fast into the position at slow
                nums[slow] = nums[fast]
        # return the count of unique elements (slow is index, so add 1 for length)
        return slow + 1

  #Time Complexity: O(N)
