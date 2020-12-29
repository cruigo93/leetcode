from typing import List


class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            # print(n)
            if n % 2 == 0:
                m = n // 2
                n = n // 2
            else:
                m = (n - 1) // 2
                n = (n - 1) // 2 + 1
            matches += m
        return matches


def main():
    sol = Solution()
    n = 14
    print(sol.numberOfMatches(n))


if __name__ == "__main__":
    main()