class solution:
	def middleNode(self,head:Listnode | None)->Listnode |None:
		temp=temp1=head
		while(temp1 and temp1.next):
			temp=temp.next
			temp1=temp1.next.next
		return temp 