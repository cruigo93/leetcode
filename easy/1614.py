from typing import List


class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        diff = 0
        m = 0
        for i in range(len(s)):
            c = s[i]
            if c == ")":
                diff -= 1
            if c == "(":
                diff += 1
            if m < diff:
                m = diff
        return m


def main():
    sol = Solution()
    s = "1"
    print(sol.maxDepth(s))


if __name__ == "__main__":
    main()