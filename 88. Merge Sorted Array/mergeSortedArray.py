class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Start filling nums1 from the end
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        k = m + n - 1  # Fill position in nums1

        # Merge while both arrays have elements
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining elements from nums2 (if any)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
