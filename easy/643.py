from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = 0
        running_avg = 0
        avgs = []
        for i in range(len(nums)):
            running_avg += nums[i]
            if i >= k:
                running_avg -= nums[i-k]
            if (i+1) >= k:
                avgs.append(running_avg / k)
        max_avg = max(avgs)
        return max_avg


def main():
    s = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(s.findMaxAverage(nums, k))


if __name__ == "__main__":
    main()