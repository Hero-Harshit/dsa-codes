class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        diff = [0] * (n + 1)

        # Mark coverage of existing bulbs
        for pos, rng in enumerate(lights):
            if rng > 0:
                left = max(0, pos - rng)
                right = min(n - 1, pos + rng)

                diff[left] += 1
                diff[right + 1] -= 1

        covered = [False] * n
        active = 0

        for i in range(n):
            active += diff[i]
            covered[i] = active > 0

        ans = 0
        idx = 0

        while idx < n:
            if covered[idx]:
                idx += 1
                continue

            ans += 1

            # New bulb covers idx, idx+1, idx+2
            idx += 3

        return ans