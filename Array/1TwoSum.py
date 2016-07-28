class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [2, 7, 11, 15]
        target = 9
        l = {}
        for i, num in enumerate(nums):
            if(target - num) in l:
                print [i, l[target-num]]
                break
            l[num] = i
