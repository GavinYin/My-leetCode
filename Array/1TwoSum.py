class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = {}
        for i, num in enumerate(nums):
            if (target - num) in l:
                return [i,l[target-num]]
            l[num] = i
