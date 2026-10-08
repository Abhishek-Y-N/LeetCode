class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        size=len(arr)
        if size%2==1:
            i=size//2
            return arr[i]
        i=len(arr)//2
        return (arr[i]+arr[i-1])/2
