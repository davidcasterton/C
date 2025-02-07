class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ['a', 'e', 'i', 'o', 'u'] # vowels
        m = len([x for x in s[:k] if x in v]) # max
        m_ = m # running max
        for i in range(k, len(s)):
            if s[i] in v:
                m_ += 1
            if s[i-k] in v:
                m_ -= 1
            if m_ > m:
                m = m_
        return m
