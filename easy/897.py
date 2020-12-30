from typing import List
from collections import defaultdict
import time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node, vals):
        if not node:
            return
        self.inorder(node.left, vals)
        vals.append(node.val)
        self.inorder(node.right, vals)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []
        self.inorder(root, vals)
        head = curr = TreeNode(0)
        for i in range(len(vals)):
            curr.right = TreeNode(val=vals[i])
            curr = curr.right
        return head.right


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

    order = sol.increasingBST(root)
    print(order.val)


if __name__ == "__main__":
    main()