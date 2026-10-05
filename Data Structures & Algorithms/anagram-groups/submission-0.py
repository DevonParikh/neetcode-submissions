class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {} # maps string : list
        l = []
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in m:
                m[sortedString].append(string)
            else:
                m[sortedString] = [string]
        for key in m:
            l.append(m[key])
        return l
