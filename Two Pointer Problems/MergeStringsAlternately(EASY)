''' 
You are given two strings word1 and word2. Merge the strings 
by adding letters in alternating order, starting with word1. If a 
string is longer than the other, append the additional letters 
onto the end of the merged string. Return the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # create 2 pointers for each string
        left1 = 0
        left2 = 0
        # create list to store charcters
        merge = []
        # while the pointer index is less than the length of the string
        while left1 < len(word1) and left2 < len(word2):
            # merge charcter into list 
            merge.append(word1[left1])
            merge.append(word2[left2])
            # move pointers to the next index
            left1 += 1
            left2 += 1
        # merge any remainder charcters in the string
        merge.append(word1[left1:])
        merge.append(word2[left2:])
        # return list as a string
        return ''.join(merge)
# Time Complexity = O(n + m)
# n = len(word1)
# m = len(word2)
