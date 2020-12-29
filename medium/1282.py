from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in groups:
                groups[groupSizes[i]].append(i)
            else:
                groups[groupSizes[i]] = [i]
        gs = []
        for k, v in groups.items():
            if k < len(v):
                g = []
                for i in range(len(v)):
                    if len(g) == k:
                        gs.append(g)
                        g = []
                    g.append(v[i])
                    # print(g)
                if len(g) > 0:
                    gs.append(g)
            else:
                gs.append(v)
        return gs



def main():
    s = Solution()
    nums = [int(f) for f in str(input()).split(",")]
    print(s.groupThePeople(nums))


if __name__ == "__main__":
    main()