class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        w = m+n-1
        i = m-1
        k = n-1

        # for i in range(i, -1, -1):
            # for k in range(k, -1, -1):
        while w >= 0:
            print(i, k, w, nums1, nums2)
            if k < 0:
                print(f'adding {nums1[i]=}')
                nums1[w] = nums1[i]
                i -= 1
            elif i < 0:
                print(f'adding {nums2[k]=}')
                nums1[w] = nums2[k]
                k -= 1
            elif nums2[k] > nums1[i]:
                print(f'adding {nums2[k]=}')
                nums1[w] = nums2[k]
                k -= 1
            else:
                print(f'adding {nums1[i]=}')
                nums1[w] = nums1[i]
                i -= 1

            w -= 1
