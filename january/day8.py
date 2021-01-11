from typing import List
from collections import defaultdict


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = "".join(word1)
        s2 = "".join(word2)
        return s1 == s2





def main():
    s = Solution()
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(s.arrayStringsAreEqual(word1, word2))


if __name__ == "__main__":
    main()