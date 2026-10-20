class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        post = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):
            pre.append(nums[i] * pre[i-1])
        for i in range(len(nums)-2, -1, -1):
            post[i] = nums[i] * post[i+1]

        output = [post[1]]
        for i in range(1, len(nums) - 1):
            output.append(pre[i-1]*post[i+1])
        output.append(pre[-2])
        return output