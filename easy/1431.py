from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = 0
        for c in candies:
            if c > max_c:
                max_c = c
        greatest = []
        for c in candies:
            if c + extraCandies >= max_c:
                greatest.append(True)
            else:
                greatest.append(False)
        return greatest


def main():
    s = Solution()
    nums = [int(f) for f in str(input()).split(",")]
    e = int(input())
    print(s.kidsWithCandies(nums, e))


if __name__ == "__main__":
    main()