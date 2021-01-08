from typing import List
from collections import defaultdict


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = [0] + arr
        n = k
        prev_k = 0
        for i in range(len(arr)-1):
            d = arr[i+1] - arr[i]
            prev_k = k
            k -= d - 1
            if k < 1:
                return prev_k + arr[i]

        return arr[-1] + k

def main():
    s = Solution()
    arr = [1, 2, 3, 4]
    k = 2

    print(s.findKthPositive(arr, k))


if __name__ == "__main__":
    main()