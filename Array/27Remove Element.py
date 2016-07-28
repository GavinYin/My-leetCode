class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 
        length = len(nums)
        lenth = 0
        while i < length:
            if nums[i] != val:
                nums[lenth] = nums[i]
                lenth = lenth +1
            i=i+1
        return lenth
        