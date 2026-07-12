from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))

        vals = [x[0] for x in arr]
        idx = [x[1] for x in arr]

        pos = [0] * n
        comp = [0] * n

        cid = 0
        pos[idx[0]] = 0
        comp[0] = cid

        for i in range(1, n):
            pos[idx[i]] = i
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # farthest reachable in one edge
        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j
            if j == i:
                j += 1
                if j > n - 1:
                    j = n - 1

        LOG = (n).bit_length()
        up = [nxt]
        for _ in range(LOG - 1):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if pu > pv:
                pu, pv = pv, pu

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            cur = pu
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < pv:
                    cur = up[k][cur]
                    steps += 1 << k

            ans.append(steps + 1)

        return ans