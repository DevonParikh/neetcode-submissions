class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(filter(str.isalnum, s)).lower()
        rev = t[::-1]
        return t == rev