from typing import List
from collections import deque
import time


class Solution:

    def is_anagram(self, s1, s2):
        d = {}
        for c in s1:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in s2:
            if c in d:
                d[c] -= 1
            else:
                d[c] = -1
        for k, v in d.items():
            if v != 0:
                return False
        return True

    def minSteps(self, s: str, t: str) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        queue = deque()
        queue.append(s)
        d = 1
        while queue:
            l = len(queue)
            d += 1
            while l > 0:
                n = queue.popleft()

                if self.is_anagram(n, t):
                    return d
                for c in alphabet:
                    for i in range(len(n)):
                        new_word = n[:i] + c + n[i+1:]
                        queue.append(new_word)
                l -= 1
            print(queue)
            time.sleep(0.5)
        return 0




def main():
    sol = Solution()
    s = "leetcode"
    t = "practice"
    print(sol.minSteps(s, t))


if __name__ == "__main__":
    main()