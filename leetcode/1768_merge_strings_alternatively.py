class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""

        for i in range(max(len(word1), len(word2))):
            try:
                out += word1[i]
            except IndexError:
                pass

            try:
                out += word2[i]
            except IndexError:
                pass

        return out
