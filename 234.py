# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def isPalindrome(self,head: LinstNode | None)->bool:
		slow=fast=head
		while fast and fast.next:
			slow=slow.next
			fast=fast.next.next

		temp=None
		while slow:
			newnode=slow.next
			slow.next=temp
			temp=slow
			slow=newnode

		while temp:
			if temp.val!=head.val:
				return False
			temp=temp.next
			head=head.next
			
		return True