# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # create left pointer
        left = 0
        # create right pointer
        right = len(s) - 1
        # check when pointers meet
        while left < right:
            # assuming they will not be the same because we are allowed to skip 1 char
            if s[left] != s[right]:
                # skip char
                skipL = s[left + 1: right+1]
                skipR = s[left:right]
                # return result of skipping char
                return (skipL[::-1] == skipL) or (skipR[::-1] == skipR)
            # move pointers
            left += 1
            right -= 1
        # return true if strings match
        return True

# Time Complexity: O(N)
