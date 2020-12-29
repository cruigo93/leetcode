from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p = head
        d = 0
        while p:
            d += 1
            p = p.next
        # print(d)
        p = head
        s = 0
        while p:
            s += (2**(d-1))*p.val
            d = d - 1
            p = p.next
            # print(s)
        return s


def main():
    sol = Solution()
    n1 = ListNode(val=1)
    n2 = ListNode(val=0)
    n3 = ListNode(val=1)
    n1.next = n2
    # n2.next = n3
    print(sol.getDecimalValue(n2))


if __name__ == "__main__":
    main()