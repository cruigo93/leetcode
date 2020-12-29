from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        for l in range(1, len(arr)+1, 2):
            for i in range(0, len(arr)-l+1):
                s += sum(arr[i:i+l])
        return s


def main():
    sol = Solution()
    arr = [10,11,12]
    print(sol.sumOddLengthSubarrays(arr))


if __name__ == "__main__":
    main()