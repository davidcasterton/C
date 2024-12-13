class Solution:
    def romanToInt(self, s: str) -> int:
        m1 = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        m2 = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        c = 0
        i = 0

        while i < len(s):
            try:
                # print(f'{s[i:i+2]=} {m2.get(s[i:i+2])=} {m2.get(s[i:i+2], m1.get(s[i], 0))=}')
                d = m2.get(s[i:i+2], 0)
                if d:
                    c += d
                    i += 1
                else:
                    c += m1.get(s[i], 0)
            except IndexError:
                c += m1.get(s[i], 0)

            i += 1

        return c
