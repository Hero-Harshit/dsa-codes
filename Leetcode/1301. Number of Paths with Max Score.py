from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        NEG = -10**9
        best = [[NEG] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        # Start from S
        best[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                max_score = NEG
                count = 0

                for ni, nj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if ni < n and nj < n and ways[ni][nj] > 0:
                        if best[ni][nj] > max_score:
                            max_score = best[ni][nj]
                            count = ways[ni][nj]
                        elif best[ni][nj] == max_score:
                            count = (count + ways[ni][nj]) % MOD

                if count == 0:
                    continue

                value = 0
                if board[i][j].isdigit():
                    value = int(board[i][j])

                best[i][j] = max_score + value
                ways[i][j] = count

        if ways[0][0] == 0:
            return [0, 0]

        return [best[0][0], ways[0][0]]