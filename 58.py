class solution:
	def lengthOfLAstWord(self,s:str)->int:
		word=s.split()
		return len(word[-1])