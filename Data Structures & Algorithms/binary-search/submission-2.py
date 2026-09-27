class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            i = int((left+right)/2)
            if target == nums[i]:
                return i
            elif target < nums[i]:
                right = i
            else:
                left = i+1
        return -1
