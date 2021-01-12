from typing import List
from collections import defaultdict



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m
        q = n
        last = m + n - 1
        while p > 0 and q > 0:
            if nums1[p-1] > nums2[q-1]:
                nums1[last] = nums1[p-1]
                p -= 1
            else:
                nums1[last] = nums2[q-1]
                q -= 1
            last -= 1
        while q > 0:
            nums1[last] = nums2[q-1]
            q -= 1
            last -= 1





def main():
    sol = Solution()
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    sol.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == "__main__":
    main()