from typing import List
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        q = head
        list_dict = defaultdict(list)
        while q:
            list_dict[q.val].append(q)
            q = q.next
        res = new_head = ListNode(0)
        for k, v in list_dict.items():
            if len(v) > 1:
                continue
            for l in v:
                l.next = None
                res.next = l
                res = res.next
        p = new_head
        while p:
            p = p.next
        return new_head.next

def main():
    s = Solution()
    nums = [1,2,2]
    l = None
    head = None
    for i in nums:
        if not l:
            l = ListNode(val=i)
            head = l
        else:
            new_node = ListNode(val=i)
            l.next = new_node
            l = l.next

    print(s.deleteDuplicates(head))


if __name__ == "__main__":
    main()