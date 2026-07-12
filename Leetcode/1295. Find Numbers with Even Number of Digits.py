class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            i = str(i)

            if len(i)%2==0:
                total += 1
        return total
