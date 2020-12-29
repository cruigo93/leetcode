from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {
            "R": 0,
            "L": 0
        }
        k = 0
        for i in range(len(s)):
            c = s[i]
            d[c] += 1
            if d["R"] == d["L"]:
                k += 1
                d["R"] = 0
                d["L"] = 0
        return k



def main():
    sol = Solution()
    s = "RLRRRLLRLL"
    print(sol.balancedStringSplit(s))


if __name__ == "__main__":
    main()