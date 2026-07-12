class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        count = 0

        for j in range(len(nums)):

            if nums[j] == val:
                pass
            else:
                nums[j], nums[i] = nums[i], nums[j]
                count += 1
                i+=1

        return count    

