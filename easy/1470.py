from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        output = []
        while i < n:
            p = nums[i]
            q = nums[i+n]
            output.append(p)
            output.append(q)
            i += 1
        return output



def main():
    s = Solution()
    nums = [int(f) for f in str(input()).split(",")]
    e = int(input())
    print(s.shuffle(nums, e))


if __name__ == "__main__":
    main()