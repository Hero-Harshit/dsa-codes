from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        # Store positions and values of non-zero digits
        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        # Powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix hash (concatenated value modulo MOD)
        prefixHash = [0] * (n + 1)
        for i in range(n):
            prefixHash[i + 1] = (prefixHash[i] * 10 + digits[i]) % MOD

        # Prefix digit sums
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            length = right - left + 1

            x = (prefixHash[right + 1] -
                 prefixHash[left] * pow10[length]) % MOD

            digitSum = prefixSum[right + 1] - prefixSum[left]

            ans.append((x * digitSum) % MOD)

        return ans