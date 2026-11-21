class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i=0
        j=len(nums)-1
        count=0
        while i < j:
            if nums[j] == 0:
                j -= 1
            elif nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                count += 1
                i += 1
                j -= 1
            else:
                i += 1
                
        return count
