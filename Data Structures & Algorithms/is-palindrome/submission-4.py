class Solution:
    def alnum(self, char: str) -> bool:
        return char.isalnum()
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        while L<R:
            while L<R and not self.alnum(s[L]):
                L+=1
            while L<R and not self.alnum(s[R]):
                R-=1
            if s[L].lower() != s[R].lower():
                return False
            else:
                L+=1
                R-=1
        return True