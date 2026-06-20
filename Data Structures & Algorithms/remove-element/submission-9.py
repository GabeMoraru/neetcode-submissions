class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        leng = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                count += 1
        nums = nums.sort()
        return leng - count