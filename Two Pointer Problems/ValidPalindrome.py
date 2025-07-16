# Problem Statement: Given a string s, return true if it is a palindrome, or false otherwise.
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove Non-alphanumeric values and convert to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # Create two pointers
        # Left starts at the beginning
        left = 0
        # Right Starts at the end
        right = len(s) - 1
        # The while loop checks the positioning of the pointers until they meet
        while left < right:
            # Compare values at the beginning and end
            if s[left] == s[right]:
                # Move the left pointer forward
                left +=1
                # Move the right pointer backwards
                right -= 1
            # If the values do not match, return false
            else:
                return False
        # If all values match, return true
        return True
# Time Complexity: O(N)
