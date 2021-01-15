from typing import List


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1]
        for i in range(1, len(n)):
            el = 2 * i
            nums.append(nums[i])

        return 1


def main():
    sol = Solution()
    n = 7
    print(sol.getMaximumGenerated(n))


if __name__ == "__main__":
    main()