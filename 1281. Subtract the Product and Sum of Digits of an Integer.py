class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        product=1
        while n:
            n, remainder = divmod(n, 10)
            sum += remainder
            product *= remainder
        return product - sum