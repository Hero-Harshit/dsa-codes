class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:

        ranges = []
        max_range = 0

        for num in nums:
            s = str(num)
            curr_range = int(max(s)) - int(min(s))
            ranges.append(curr_range)
            if curr_range > max_range:
                max_range = curr_range

        sum = 0
        for i in range(len(nums)):

            if ranges[i] == max_range:
                sum = sum + nums[i]

        return sum
        
        
  