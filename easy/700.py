from typing import List
from collections import defaultdict
import time
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr_head = root
        queue = [curr_head]
        while queue:
            curr_head = queue.pop(0)
            if curr_head.val == val:
                return curr_head
            if curr_head.left:
                if curr_head.val > val:
                    queue.append(curr_head.left)
            if curr_head.right:
                if curr_head.val < val:
                    queue.append(curr_head.right)
        return None




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

    val = 2
    print(sol.searchBST(root, val).val)


if __name__ == "__main__":
    main()