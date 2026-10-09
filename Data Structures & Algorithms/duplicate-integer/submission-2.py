class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set() # numbers
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False