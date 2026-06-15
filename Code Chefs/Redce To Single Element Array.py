def canReduce(N: int, arr: list[int]) -> bool:
        arr.sort()
        
        for i in range(N - 1):
            if arr[i + 1] - arr[i] > 1:
                return False

        return True