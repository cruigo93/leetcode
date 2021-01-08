from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
        k = 0
        max_k = 0
        q = 0
        p = 0
        while p < len(s):
            c = s[p]
            if c in seen and seen[c] >= q:
                q = seen[c] + 1
            k = p - q + 1
            if k > max_k:
                max_k = k
            seen[c] = p
            p += 1

        return max_k





def main():
    s = Solution()
    string = input()

    print(s.lengthOfLongestSubstring(string))


if __name__ == "__main__":
    main()