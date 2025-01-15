class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vm = {} # map of vowel index : vowel letter

        # build map of vowels to index
        for i in range(len(s)):
            if s[i].lower() in vowels:
                vm[i] = s[i]

        # no vowels, return original
        if not vm:
            return s

        # replace vowels
        vmi = sorted(list(vm.keys()))
        out = ""

        print(f'{vm=} {vmi=}')

        for i in range(len(vmi)):
            if i==0:
                out += s[:vmi[i]] + vm[vmi[-(i+1)]]
            else:
                out += s[vmi[i-1]+1:vmi[i]] + vm[vmi[-(i+1)]]
        try:
            out +=  s[vmi[i]+1:]
        except IndexError:
            pass

        return out
