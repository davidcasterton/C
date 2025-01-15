class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = -1
        nlen = len(needle)
        hlen = len(haystack)

        # # naive O(n)
        # for i in range(len(haystack) - nlen):
        #     if haystack[i:i+nlen] == needle:
        #         idx = i
        #         break

        # find indexes in haystack of first letter of needle, then search
        f = [_idx for _idx, c in enumerate(haystack) if c == needle[0]]
        # print(f'{f=}')
        for i in f:
            # print(f'{i+nlen} <= {hlen} and {haystack[i:i+nlen]} == {needle}')
            if i+nlen <= hlen and haystack[i:i+nlen] == needle:
                idx = i
                break

        return idx
