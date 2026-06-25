from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        prefix = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            prefix.append(s)

        ans = 0
        for j in range(1, n + 1):
            for i in range(j):
                if prefix[i] < prefix[j]:
                    ans += 1

        return ans
        
        