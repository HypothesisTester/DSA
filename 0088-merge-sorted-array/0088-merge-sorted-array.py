class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = j = 0
        merged = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        merged.extend(nums1[i:m])
        merged.extend(nums2[j:n])
        nums1[:m+n] = merged

