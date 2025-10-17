class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []

        for i in range(m):
            nums3.append(nums1[i])
        
        if (n != 0):
            for i in range(n):
                nums3.append(nums2[i])

        nums3.sort()

        del nums1[:]
        nums1.extend(nums3)

        