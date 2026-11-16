# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nextclass Solution:
def getDecimalValue(self,head: ListNode | None)->int:
	decimal=0
	while head:
		decimal=decimal*2+head.val
		head=head.next
		
	return decimal