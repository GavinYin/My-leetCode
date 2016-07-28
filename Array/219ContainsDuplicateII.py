class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                dif = i - dic[nums[i]]
                if dif <= k:
                    return True
                dic[nums[i]] = i
        return False