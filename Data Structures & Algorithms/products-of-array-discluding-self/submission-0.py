class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums[0] != 0:
            res = [nums[0]]
            index = []
        else:
            res = [1]
            index = [0]
        for i in range(1, len(nums)):
            if nums[i] != 0:
                res.append(nums[i] * res[i-1])
            else:
                res.append(res[i-1])
                index.append(i)
        prod = res[-1]
        if len(index) == 1:
            output = [0] * len(nums)
            output[index[0]] = prod
        elif len(index) > 1:
            output = [0] * len(nums)
        else:
            output = [res[-1]] * len(nums)
            for i, num in enumerate(nums):
                output[i] //= num
        return output
