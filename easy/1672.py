from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(len(accounts)):
            s = 0
            for j in range(len(accounts[i])):
                s += accounts[i][j]
            if s > wealth:
                wealth = s
        return wealth


def main():
    s = Solution()
    nums = [int(f) for f in str(input()).split()]
    print(s.runningSum(nums))


if __name__ == "__main__":
    main()