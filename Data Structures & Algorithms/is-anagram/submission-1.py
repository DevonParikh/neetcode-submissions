class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        u = t #copy t so doesn't change input string
        for char in s:
            if char not in u:
                return False
            u = u[0:u.index(char)] + u[u.index(char)+1:] #deletes char from u
        return True