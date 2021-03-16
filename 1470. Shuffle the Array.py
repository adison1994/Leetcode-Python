class Solution(object):
    def shuffle(self, nums, n):
        res = []
        for i, j in zip(nums[:n],nums[n:]):
            res += [i,j]
        return res
            