class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        l = len(arr)
        counts = []
        out = True
        last = None

        i = 0
        while i < l:
            if arr[i] == last:
                i += 1
                continue
            last = arr[i]
            c = 1
            for k in range(i+1, l):
                if arr[k] == arr[i]:
                    c += 1
                else:
                    i = k-1
                    break
            i += 1
            if c in counts:
                out = False
                break
            else:
                counts.append(c)
        return out
