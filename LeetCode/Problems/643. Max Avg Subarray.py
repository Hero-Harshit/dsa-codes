class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_avg = float("-inf")

        if len(nums)<k:
            return ((sum[nums])/k)

        for i in range(len(nums)-k+1):
            sum = 0

            for j in range(k):
                sum += nums[j+i]

            avg = sum/k

            if avg > max_avg:
                max_avg = avg

        return max_avg             

Now the above method was brute force but the next one uses sliding window protocol.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if len(nums)<k:
            return ((sum[nums])/k)

        max_avg = sum(nums[:k])/k
        current_sum = sum(nums[:k])
        for i in range(len(nums)-k):

            current_sum += nums[k+i] - nums[i]
            if max_avg<current_sum/k:
                max_avg = current_sum/k

        return max_avg             