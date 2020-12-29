from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        k = 0
        for i in range(len(words)):
            if len(set(words[i]).union(set(allowed))) == len(allowed):
                k += 1
        return k



def main():
    s = Solution()
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(s.countConsistentStrings(allowed, words))


if __name__ == "__main__":
    main()