'''

Create linked list and remove nth node

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    
    slow = head
    fast = head
    
    for i in range(0, n):
        if fast.next is None:
           
            if i == n - 1:
                head = head.next
            return head
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    if slow.next is not None:
        slow.next = slow.next.next
    return head




z = ListNode(3)
y = ListNode(2, z)
x = ListNode(1, y)






print(removeNthFromEnd(x, 2))
