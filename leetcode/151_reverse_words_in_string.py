class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")  # split into list of words
        # words = [w for w in words if w]  # remove empties
        words_reversed = " ".join([words[-(i+1)] for i in range(len(words)) if words[-(i+1)]])  # reverse list of words then join into string
        return words_reversed
