# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # create pointer on left 
        left = 0
        # create pointer on right 
        right = len(s) - 1
        # while left index is less than right
        while left < right:
            # swap left value with right
            s[left], s[right] = s[right], s[left]
            # move pointer forward
            left += 1
            # move pointer backwards
            right -= 1
