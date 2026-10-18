class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        output = []
        for i, num in enumerate(nums2):
            m[num] = i
        for num in nums1:
            j = m[num]
            for i in range(j, len(nums2)):
                if nums2[i] > num:
                    output.append(nums2[i])
                    break
                if i == len(nums2)-1:
                    output.append(-1)
        return output