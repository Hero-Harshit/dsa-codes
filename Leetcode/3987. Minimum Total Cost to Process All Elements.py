class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:

        MOD = 10**9 + 7
        resources = k
        recharges = 0

        d = list(nums)
        
        for need in d:

            if resources < need:
                deficit = need - resources

                needed_recharges = (deficit + k -1) // k
                recharges += needed_recharges
                resources += needed_recharges*k

            resources -= need
            
        cost = (recharges * (recharges +1)) // 2
        return cost % MOD