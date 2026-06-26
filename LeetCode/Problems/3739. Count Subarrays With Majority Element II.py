from typing import List
from bisect import bisect_left

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref = [0]
        s = 0
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            pref.append(s)

        vals = sorted(set(pref))
        bit = BIT(len(vals))

        ans = 0
        for x in pref:
            idx = bisect_left(vals, x) + 1
            ans += bit.query(idx - 1)      # previous prefix sums < current
            bit.add(idx, 1)

        return ans