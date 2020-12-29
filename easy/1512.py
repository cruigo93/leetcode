from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    k += 1
        return k


def main():
    s = Solution()
    nums = [int(f) for f in str(input()).split(",")]
    print(s.numIdenticalPairs(nums))


if __name__ == "__main__":
    main()