from typing import List

def xor(a, b):
    print(a, b)
    return (a and not b) or (not a and b)

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        x1 = start
        for i in range(n):
            x2 = x1 + 2 * i
            res = xor(bin(x1), bin(x2))
            x1 = x2
        return res


def main():
    sol = Solution()
    n = 5
    start = 0
    print(sol.xorOperation(n, start))


if __name__ == "__main__":
    main()