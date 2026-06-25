class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = 0
        second = 0
        for i in range(len(nums)):
            temp = max(nums[i] + first, second)
            first = second
            second = temp
        return second