from typing import List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


def main():
    s = Solution()
    num = 1
    print(s.isPowerOfThree(num))


if __name__ == "__main__":
    main()