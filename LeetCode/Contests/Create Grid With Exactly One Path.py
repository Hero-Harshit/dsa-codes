class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []

        for i in range(m):
            curr_row = []
            for j in range(n):
                if i == 0 or j == n-1:
                    curr_row.append(".")
                else:
                    curr_row.append("#")
            grid.append(''.join(curr_row))

        return grid
                            