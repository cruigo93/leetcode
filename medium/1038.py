from typing import List
from collections import defaultdict
import time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node, vals, nodes):
        if not node:
            return
        self.inorder(node.right, vals, nodes)
        vals.append(node.val)
        nodes.append(node)
        self.inorder(node.left, vals, nodes)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        vals = []
        nodes = []
        self.inorder(root, vals, nodes)
        # print(vals)
        head = curr = TreeNode(0)
        running_sum = 0
        for i in range(len(vals)):
            running_sum += vals[i]
            nodes[i].val = running_sum
        return root


def main():
    sol = Solution()
    root = TreeNode(val=4)
    l1 = TreeNode(val=2)
    r1 = TreeNode(val=7)
    l2 = TreeNode(val=1)
    r2 = TreeNode(val=3)

    root.right = r1
    root.left = l1

    l1.left = l2
    l1.right = r2

    order = sol.bstToGst(root)
    print(order.val)


if __name__ == "__main__":
    main()