# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseList(self,head : Listnode | None)->Listnode | None:
		temp=head
		if temp==None:
			return
		li=[]
		while(temp):
			li.append(temp.val)
			temp=temp.next
		temp=head

		for i in range(len(li)-1,-1,-1):
			li.append(temp.val)
			temp=temp.next

		return head
		 