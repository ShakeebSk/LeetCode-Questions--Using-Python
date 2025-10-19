class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged=nums1+nums2
        merged.sort()
        if len(merged)%2==0:
            return (merged[len(merged)/2]+merged[len(merged)/2-1])/2.0
        else :
            return merged[len(merged)/2]
