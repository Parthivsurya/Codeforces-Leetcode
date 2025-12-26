from traitlets import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        print(n)
        if n % 2 != 0:
            print(nums1[n//2])
        else:
            print((nums1[n//2] + nums1[n//2 - 1]) / 2)
sl=Solution()
print(sl.findMedianSortedArrays([1,3],[0,5]))
