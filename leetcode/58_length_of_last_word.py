class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0

        _s = s.strip()

        for i in range(len(_s)):
            if _s[-(i+1)] == " ":
                break
            c += 1

        return c
