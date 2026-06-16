class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0

        for i in range(len(nums)):
            nums[i] = nums[i]+sum
            sum = nums[i]

        return nums    