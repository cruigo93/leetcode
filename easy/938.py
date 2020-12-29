from typing import List
import time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def constract_tree(arr):
#     curr_head = None
#     root = None
#     for i in range(len(arr)):
#         if not root:
#             curr_head = TreeNode(arr[i])
#             root = curr_head
#         else:
#             if arr[i] > curr_head.val:
#                 curr_head.left
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        queue = [root]
        start = 0
        end = 1
        s = 0
        while start < end:
            c = queue[start]
            start += 1
            if high >= c.val >= low:
                s += c.val
            # if c.val <= low:
            if c.right:
                queue.append(c.right)
                end += 1
            # if c.val >= high:
            if c.left:
                queue.append(c.left)
                end += 1
        return s



def main():
    sol = Solution()
    root = TreeNode(val=10)
    l1 = TreeNode(val=5)
    r1 = TreeNode(val=15)
    l2 = TreeNode(val=3)
    r2 = TreeNode(val=7)
    r3 = TreeNode(val=18)

    root.left = l1
    root.right = r1
    l1.left = l2
    l2.right = r2
    r1.right = r3
    high = 15
    low = 7
    print(sol.rangeSumBST(root, low, high))


if __name__ == "__main__":
    main()