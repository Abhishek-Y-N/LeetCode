class Solution:
	def digigtFrequencyScore(self,n: int)->int:
		freq={}
		total=0

		while(n):
			ld=n%10
			if ld in freq:
				freq[ld]+=1
			else:
				freq[ld]=1
			n//=10

		for i in freq:
			total+=freq[i]*i

		return total