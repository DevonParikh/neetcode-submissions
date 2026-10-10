class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = True

        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            elif rotated:
                rotated = False
            else:
                return False
        if nums[-1] > nums[0] and not rotated:
            return False
        return True