class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s = []
        l = len(nums)
        k = k % l
        for i in range(k):
        	s.insert(0,nums[l-i-1])
        for j in range(k,l):
        	s.append(nums[j-k])
        for m in range(l):
        	nums[m] = s[m]
        return 

############################################第二种方法
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = []
        l = nums[0:k-1]
        l.reverse()
        nums = nums[k:l-1]
        nums.reverse()
        nums = l + nums
        nums.reverse()
        return