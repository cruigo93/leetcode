from typing import List
from collections import defaultdict


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 0
        new_digits = []
        s = digits[-1] + 1
        c = s // 10
        s = s % 10
        new_digits.append(s)
        for i in range(len(digits)-2, -1, -1):
            s = digits[i] + c
            c = s // 10
            s = s % 10
            new_digits.append(s)
        if c > 0:
            new_digits.append(c)
        return new_digits[::-1]





def main():
    s = Solution()
    nums = [2,9,9]
    print(s.plusOne(nums))


if __name__ == "__main__":
    main()