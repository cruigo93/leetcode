from typing import List
from collections import defaultdict


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l = 0
        for i in range(len(nums)):
            if nums[i] > nums[l]:
                l = i
        for i in range(len(nums)):
            if nums[i] * 2 > nums[l] and i != l:
                return -1
        return l





def main():
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.dominantIndex(nums))


if __name__ == "__main__":
    main()