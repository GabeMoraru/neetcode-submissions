class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest = 0
        running = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                running += 1
            else:
                running = 0
            if running > highest:
                highest = running
        return highest
