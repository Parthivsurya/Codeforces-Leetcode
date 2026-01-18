def removeNthFromEnd(self, head: Optional[ListNode], n: int):
    def reverseList(self, head: Optional[ListNode]):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
    reverseList(head)
    while prev.next:
        if prev.next.val == n:
            prev = prev.next.next
            return prev
        else:
            prev = prev.next
        
    