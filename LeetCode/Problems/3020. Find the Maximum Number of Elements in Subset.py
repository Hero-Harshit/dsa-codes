from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in cnt:
            ans = max(ans, cnt[1] if cnt[1] % 2 else cnt[1] - 1)

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cur in cnt:
                if cnt[cur] >= 2:
                    length += 2
                    cur *= cur
                else:
                    length += 1
                    break

            # If the chain ended because the next square doesn't exist,
            # remove one from the last pair to make it the center.
            if cur not in cnt:
                length -= 1

            ans = max(ans, length)

        return ans