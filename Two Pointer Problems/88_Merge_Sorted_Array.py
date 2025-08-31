'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in 
nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.The final sorted array should not be returned 
by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # create pointer at last element in nums1
        last = m + n - 1
        # while the pointer is not at the end
        while n > 0 and m > 0:
            # if last int in nums1 is greater than last int in nums2
            if nums1[m - 1] > nums2[n - 1]:
                # since last int in nums1 is greater than last int in nums2 move to back of nums1 (0)
                nums1[last] = nums1[m - 1]
                # move pointers back
                m -= 1
                last -= 1
            # else last int in nums1 is less than or equal to int in nums2
            else:
                # add nums2 int to back of nums1
                nums1[last] = nums2[n - 1]
                # move pointers
                n -= 1
                last -= 1
        # while n still has elements
        while n > 0:
            # add remainders to back of nums1
            nums1[last] = nums2[n-1]
            # move pointers back
            last -= 1
            n -= 1


# Time Complexity: O(M+N)
