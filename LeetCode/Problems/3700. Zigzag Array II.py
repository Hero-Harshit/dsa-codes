class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        size = 2 * m

        # State:
        # A[x] = number of valid arrays ending with (..., a, x) where a > x
        # B[x] = number of valid arrays ending with (..., a, x) where a < x
        #
        # Transitions:
        # B'[x] = sum(A[y] for y < x)
        # A'[x] = sum(B[y] for y > x)

        M = [[0] * size for _ in range(size)]

        # A' = S * B
        for x in range(m):
            row = M[x]
            for y in range(x + 1, m):
                row[m + y] = 1

        # B' = P * A
        for x in range(m):
            row = M[m + x]
            for y in range(x):
                row[y] = 1

        def mat_mul(A, B):
            nsz = len(A)
            R = [[0] * nsz for _ in range(nsz)]

            for i in range(nsz):
                Ri = R[i]
                Ai = A[i]
                for k in range(nsz):
                    if Ai[k] == 0:
                        continue
                    aik = Ai[k]
                    Bk = B[k]
                    for j in range(nsz):
                        if Bk[j]:
                            Ri[j] = (Ri[j] + aik * Bk[j]) % MOD
            return R

        def mat_vec_mul(A, v):
            nsz = len(A)
            res = [0] * nsz
            for i in range(nsz):
                s = 0
                row = A[i]
                for j in range(nsz):
                    if row[j]:
                        s += row[j] * v[j]
                res[i] = s % MOD
            return res

        # Length = 2 initialization
        # A[x] = count of values greater than x
        # B[x] = count of values smaller than x
        vec = [m - 1 - x for x in range(m)] + [x for x in range(m)]

        power = n - 2
        base = M

        while power:
            if power & 1:
                vec = mat_vec_mul(base, vec)
            base = mat_mul(base, base)
            power >>= 1

        return sum(vec) % MOD