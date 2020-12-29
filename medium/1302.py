from typing import List
from collections import defaultdict
import time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth_dict = defaultdict(list)
        d = 0
        start = 0
        end = 1
        p = root
        queue = [p]
        depth = [0]
        while start < end:
            p = queue[start]
            d = depth[start]
            start += 1
            if p.left:
                queue.append(p.left)
                depth_dict[d + 1].append(p.left)
                end += 1
                depth.append(d + 1)
            if p.right:
                queue.append(p.right)
                depth_dict[d + 1].append(p.right)
                end += 1
                depth.append(d + 1)

        return sum([c.val for c in depth_dict[d]])



def main():
    sol = Solution()
    root = TreeNode(val=1)
    l1 = TreeNode(val=2)
    r1 = TreeNode(val=3)
    l2 = TreeNode(val=4)
    r2 = TreeNode(val=5)
    r3 = TreeNode(val=6)
    r4 = TreeNode(val=8)
    l4 = TreeNode(val=7)

    root.right = r1
    root.left = l1

    r1.right = r3
    r3.right = r4

    l1.left = l2
    l1.right = r2

    l2.left = l4

    print(sol.deepestLeavesSum(root))


if __name__ == "__main__":
    main()