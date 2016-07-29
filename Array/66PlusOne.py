class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d = []
        carry = 1
        for n in reversed(digits):
            sum = n + carry
            if sum >= 10:
                carry = sum / 10
                sum = sum - 10
            else:
                carry = 0
            d = [sum] + d
        if carry:
            d = [carry] + d
        return d

