class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        remain = max(candies) - extraCandies 
        return [candy >= remain for candy in candies]
        