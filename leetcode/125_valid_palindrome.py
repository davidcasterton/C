class Solution:
    def isPalindrome(self, s: str) -> bool:
        an = "".join([c for c in s if c.isalnum()]).lower()
        c = "".join(an.split(" "))  # collapsed string, no whitespace
        r = "".join(c[-(i+1)] for i in range(len(c))) # reversed collapsed string
        print(an, c, r)
        return c == r
