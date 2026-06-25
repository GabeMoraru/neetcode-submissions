class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        arr = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            arr.append(max(arr[:i - 1]) + nums[i])
        return max(arr)