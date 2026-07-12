class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        # All possible k values to check
        candidates = {2}

        for x in nums:
            d = 2
            while d * d <= x:
                if x % d == 0:
                    candidates.add(d)
                    candidates.add(x // d)
                d += 1
            if x > 1:
                candidates.add(x)

        best_diff = -10**18
        best_k = 2

        for k in candidates:
            cur = None
            mx = -10**18

            # Kadane's algorithm
            for x in nums:
                val = x if x % k == 0 else -x

                if cur is None:
                    cur = val
                else:
                    cur = max(val, cur + val)

                mx = max(mx, cur)

            if mx > best_diff or (mx == best_diff and k < best_k):
                best_diff = mx
                best_k = k

        return (best_diff * best_k) % MOD