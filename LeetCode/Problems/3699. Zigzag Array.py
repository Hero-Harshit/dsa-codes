class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # DP for length = 2
        U = [0] * m  # last move was up
        D = [0] * m  # last move was down

        for x in range(m):
            U[x] = x           # count of y < x
            D[x] = m - 1 - x   # count of y > x

        if n == 2:
            return sum(U + D) % MOD

        for _ in range(3, n + 1):
            newU = [0] * m
            newD = [0] * m

            # newU[x] = sum_{y < x} D[y]
            pref = 0
            for x in range(m):
                newU[x] = pref
                pref = (pref + D[x]) % MOD

            # newD[x] = sum_{y > x} U[y]
            suff = 0
            for x in range(m - 1, -1, -1):
                newD[x] = suff
                suff = (suff + U[x]) % MOD

            U, D = newU, newD

        return (sum(U) + sum(D)) % MOD
    