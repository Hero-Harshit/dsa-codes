def largestRectangleArea(N: int, A: list[int]) -> int:

    stack = []
    max_area = 0

    for i in range(N + 1):

        curr_height = 0 if i == N else A[i]

        while stack and A[stack[-1]] > curr_height:

            height = A[stack.pop()]

            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            area = height * width

            max_area = max(max_area, area)

        stack.append(i)

    return max_area