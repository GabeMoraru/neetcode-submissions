class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]


        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]

        ret = [None] * len(nums)
        ret[0] = suffix[1]
        ret[-1] = prefix[-2]
        for i in range(1, len(nums) - 1):
            ret[i] = prefix[i - 1] * suffix[i + 1]

        
        return ret