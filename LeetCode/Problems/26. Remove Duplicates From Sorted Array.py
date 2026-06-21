from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        write = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                nums[write] = nums[i]
                write += 1

        return write