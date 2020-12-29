from typing import List


class Solution:
    def toLowerCase(self, str: str) -> str:
        new_str = ""
        for i in range(len(str)):
            c = str[i]
            if ord("Z") >= ord(c) >= ord("A"):
                c = chr(ord(c) + 32)
            new_str += c

        return new_str


def main():
    sol = Solution()
    s = input()
    print(sol.toLowerCase(s))


if __name__ == "__main__":
    main()