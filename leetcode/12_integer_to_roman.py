class Solution:
    def intToRoman(self, num: int) -> str:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        mr = {v:k for k,v in m.items()}  # m dictionary reversed
        mvs = sorted(m.values(), reverse=True)  # m values reverse sorted

        s = 0  # running sum of roman numeral
        r = ""  # roman numeral
        while s < num:
            for v in mvs:
                if (s+v) <= num:
                    r += mr.get(v)
                    s += v
                    # print(f'{r=} {s=}')
                    break

        return r
