class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head and head.val == val:
            head = head.next
            
        temp = head
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
                
        return head