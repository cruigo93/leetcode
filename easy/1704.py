from typing import List


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = 0
        b = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        mid = len(s) // 2
        for i in range(len(s)):
            if s[i] in vowels:
                if i < mid:
                    a += 1
                else:
                    b += 1
        return a == b


def main():
    sol = Solution()
    s = "MerryChristmas"
    print(sol.halvesAreAlike(s))


if __name__ == "__main__":
    main()