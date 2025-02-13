from copy import deepcopy

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # max
        m = {
            'l': "", # letters
            's': 0, # start index
            'e': 0 # end index
        }
        # current
        c = {
            'l': "", # letters
            's': 0, # start index
        }

        for i in range(len(s)):
            print(f'{i=}')
            if s[i] not in c['l']:
                c['l'] += s[i]
            else:
                if len(c['l']) > len(m['l']):
                    # copy current into max
                    m = deepcopy(c)
                    m['e'] = i-1
                    print(f'new m {m=}')

                # restart current at index after last duplicate letter
                c['s'] += s[c['s']:i].index(s[i]) + 1
                c['l'] = s[c['s']:i+1]
                print(f'new c {c=}')

        if len(c['l']) > len(m['l']):
            # copy current into max
            m = deepcopy(c)
            m['e'] = len(s)
            print(f'new final m {m=}')

        return len(m['l'])
