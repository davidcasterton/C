class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 == str2:
            return str1

        out = ""
        for n in range(min(len(str1), len(str2)), 0, -1):
            # string 1 splits and equality check
            s1 = [str1[i:i+n] for i in range(0, len(str1), n)] # str1 splits
            check = all([(s1[i] == s1[i+1]) for i in range(len(s1)-1)])

            if check:
                # string 2 splits and equality check
                s2 = [str2[i:i+n] for i in range(0, len(str2), n)] # str2 splits
                s = s1 + s2
                check = all([(s[i] == s[i+1]) for i in range(len(s)-1)])

                if check:
                    out = str1[:n]
                    break
        return out
