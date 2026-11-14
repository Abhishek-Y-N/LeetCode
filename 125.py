class Solution:
	def isPalindrome(self, s: str)->bool:
		s=s.lower()
		words=""

		for i in s:
			if i.isalnum():
				words+=i

		j=len(words)-1
		for i in range(len(words)//2):
			if words[i]!=words[j]:
				return False
			j-=1

		return True