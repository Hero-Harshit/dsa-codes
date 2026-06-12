class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        new = []

        for num in nums:
            if num != val:
                new.append(num)

        for i in range(len(new)):
            nums[i] = new[i]

        return len(new)
                