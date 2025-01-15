class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pre = strs[0]

        for word in strs[1:]:
            # early exit if match
            if pre == word:
                continue

            # compare letter by letter
            for i in range( min(len(word), len(pre)) ):
                if pre[i] != word[i]:
                    pre = word[:i]
                    break

            # handle if word is shorter than current prefix
            if len(word) < len(pre):
                pre = word

        return pre
