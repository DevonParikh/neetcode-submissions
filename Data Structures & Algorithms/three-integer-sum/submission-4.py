class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i-1] == a:
                continue
            L, R = i+1, len(nums)-1
            while L < R:
                if nums[L] + nums[R] == -1 * nums[i]:
                    output.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L+=1
                    L+=1
                elif nums[L] + nums[R] > -1 * nums[i]:
                    R-=1
                elif nums[L] + nums[R] < -1 * nums[i]:
                    L+=1
        return output