from typing import List
import time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        p = root
        start = 0
        end = 1
        even_nodes = []
        queue = [p]
        if p.val % 2 == 0:
            even_nodes.append(p)

        while start < end:
            c = queue[start]
            start += 1
            if c.right:
                if c.right.val % 2 == 0:
                    even_nodes.append(c.right)
                queue.append(c.right)
                end += 1
            if c.left:
                if c.left.val % 2 == 0:
                    even_nodes.append(c.left)
                queue.append(c.left)
                end += 1
        s = 0
        # print([c.val for c in even_nodes])
        for c in even_nodes:
            if c.left:
                if c.left.left:
                    s += c.left.left.val
                if c.left.right:
                    s += c.left.right.val
            if c.right:
                if c.right.left:
                    s += c.right.left.val
                if c.right.right:
                    s += c.right.right.val
        return s



def main():
    sol = Solution()
    root = TreeNode(val=6)
    l1 = TreeNode(val=7)
    r1 = TreeNode(val=8)
    l2 = TreeNode(val=2)
    r2 = TreeNode(val=7)
    l3 = TreeNode(val=1)
    r3 = TreeNode(val=3)
    r4 = TreeNode(val=5)

    root.right = r1
    root.left = l1

    r1.left = l3
    r1.right = r3

    l1.left = l2
    l1.right = r2

    r3.right = r4

    print(sol.sumEvenGrandparent(root))


if __name__ == "__main__":
    main()