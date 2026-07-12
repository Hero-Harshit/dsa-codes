class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        writer = 0
        count = 0

        for reader in range(1, len(nums)):

            if nums[writer] != nums[reader]:
                nums[writer+1], nums[reader] = nums[reader], nums[writer+1]
                writer += 1
                count += 1

        return count+1