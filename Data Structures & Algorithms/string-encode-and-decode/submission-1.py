class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for c in s:
                res += str(ord(c))+"_"
            res += ","
        return res
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        output = [""]
        count = 0
        pos = 0
        for i in range(len(s)-1):
            if s[i] != "_" and s[i] != ",":
                count += 1
            elif s[i] == "_":
                output[pos] += chr(int(s[i-count: i]))
                count = 0
            elif s[i] == ",":
                output.append("")
                pos += 1
        return output