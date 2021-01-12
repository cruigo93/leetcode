class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        carry = 0
        curr = res
        p = l1
        q = l2
        while p or q:
            if p:
                carry = carry + p.val
                p = p.next
            if q:
                carry = carry + q.val
                q = q.next
            new_node = ListNode(carry % 10)
            curr.next = new_node
            curr = curr.next
            carry = carry // 10
        if carry > 0:
            new_node = ListNode(carry)
            curr.next = new_node

        return res.next


def main():
    sol = Solution()
    l1 = [0]
    l2 = [0]
    list1 = None
    curr = None
    for el in l1:
        if not list1:
            list1 = ListNode(el)
            curr = list1
        else:
            new_node = ListNode(el)
            curr.next = new_node
            curr = curr.next
    list2 = None
    curr = None
    for el in l2:
        if not list2:
            list2 = ListNode(el)
            curr = list2
        else:
            new_node = ListNode(el)
            curr.next = new_node
            curr = curr.next

    sum_l = sol.addTwoNumbers(list1, list2)
    print_list(sum_l)

if __name__ == "__main__":
    main()