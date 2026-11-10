class Solution:
	def alternateDigitSum(self, n: int)->int:
		even_sum=0
		odd_sum=0
		count=len(str(n))

		while(n):
			odd_sum+=n%10
			n//=10

			even_sum+=n%10
			n//=10

		if count%2:
			return odd_sum-even_sum

		return even_sum-odd_sum 