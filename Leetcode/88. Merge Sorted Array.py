class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        w = len(nums1)-1
        r1 = len(nums1)-len(nums2)-1
        r2 = len(nums2)-1

        while r1>=0 and r2>=0:

            if nums2[r2] > nums1[r1]:
                nums1[w] = nums2[r2]
                r2 -= 1
                w -= 1
            else:
                nums1[w] = nums1[r1]
                r1 -= 1
                w -= 1

        while r2 >= 0:

            nums1[w] = nums2[r2]
            r2 -= 1
            w -= 1
