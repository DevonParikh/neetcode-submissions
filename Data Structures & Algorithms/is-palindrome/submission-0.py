class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(filter(str.isalnum, s)).lower()
        first_half = t[0:len(t)//2]
        if len(t) % 2 == 0:
            second_half = t[len(t)//2:][::-1]
        else:
            second_half = t[len(t)//2 + 1:][::-1]
        return first_half == second_half