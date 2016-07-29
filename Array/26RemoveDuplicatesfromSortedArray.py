class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 1
        n = 1
        if len(nums) < 2:
            return len(nums)
        else:
            while i < len(nums):
                if nums[i-1] != nums[i]:
                    nums[n] = nums[i]
                    n = n + 1
                i = i + 1
        return n
        
        