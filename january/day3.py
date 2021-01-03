from typing import List


class Solution:
    def backtrack(self, x):
        if x == 0:
            self.count += 1
        for i in range(1, self.n+1):
            if not self.used[i] and (x % i == 0 or i % x == 0):
                self.used[i] = True
                self.backtrack(x - 1)
                self.used[i] = False

    def countArrangement(self, n: int) -> int:
        self.used = [False for i in range(n+1)]
        self.count = 0
        self.n = n
        self.backtrack(n)
        return self.count


def main():
    s = Solution()
    num = 6
    print(s.countArrangement(num))


if __name__ == "__main__":
    main()