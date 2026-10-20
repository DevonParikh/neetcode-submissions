class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        i = 1
        t = nums[0]
        while i < len(nums):
            output[i] = t
            t *= nums[i]
            i += 1
        i = len(nums) - 2
        t = nums[-1]
        while i > -1:
            output[i] *= t
            t *= nums[i]
            i -= 1
        return output