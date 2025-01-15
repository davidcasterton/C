class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0  # indices of s that have been matched
        slen = len(s)

        if not s:
            return True
        if not t:
            return False

        for i in range(len(t)):
            if s[si] == t[i]:
                si += 1
            if si == slen:
                return True

        return False
