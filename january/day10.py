from typing import List
from collections import defaultdict



class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        cost = 0
        d = {}

        for el in instructions:
            less = len([e for e in nums if e < el])
            higher = len([e for e in nums if e > el])
            c = min(less, higher)
            nums.append(el)
            cost += c
        return cost





def main():
    sol = Solution()
    instructions = [1,3,3,3,2,4,2,1,2]

    print(sol.createSortedArray(instructions))


if __name__ == "__main__":
    main()