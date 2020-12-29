from typing import List
import time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        p = original
        q = cloned
        start = 0
        end = 1
        queue = [p]
        cloned_queue = [q]
        while start < end:
            cp = queue[start]
            cq = cloned_queue[start]
            start += 1
            if cp.left:
                queue.append(cp.left)
                cloned_queue.append(cq.left)
                end += 1
            if cp.right:
                queue.append(cp.right)
                cloned_queue.append(cq.right)
                end += 1
            if cp == target:
                return cq



def main():
    sol = Solution()
    root = TreeNode(val=7)
    l1 = TreeNode(val=4)
    r1 = TreeNode(val=3)
    l2 = TreeNode(val=6)
    r2 = TreeNode(val=19)

    root.left = l1
    root.right = r1
    r1.left = l2
    r1.right = r2

    root2 = TreeNode(val=7)
    l12 = TreeNode(val=4)
    r12 = TreeNode(val=3)
    l22 = TreeNode(val=6)
    r22 = TreeNode(val=19)

    root2.left = l12
    root2.right = r12
    r12.left = l22
    r12.right = r22

    print(sol.getTargetCopy(root, root2, r1).val)


if __name__ == "__main__":
    main()