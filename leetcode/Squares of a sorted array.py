class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        right = get_min_noneg(nums)
        left = right - 1
        while right < n and left >= 0:
            if nums[left] ** 2 < nums[right] ** 2:
                res.append(nums[left] ** 2)
                left -= 1
            else:
                res.append(nums[right] ** 2)
                right += 1
        while left >= 0:
            res.append(nums[left] ** 2)
            left -= 1
        while right < n:
            res.append(nums[right] ** 2)
            right += 1
        return res


def get_min_noneg(lst):
    n = len(lst)
    for i in range(n):
        if lst[i] >= 0:
            return i
    return n