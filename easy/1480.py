from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = [nums[0]]
        for i in range(1, len(nums)):
            running_sums.append(running_sums[i-1] + nums[i])
        return running_sums


def main():
    s = Solution()
    nums = [int(f) for f in str(input()).split()]
    print(s.runningSum(nums))


if __name__ == "__main__":
    main()