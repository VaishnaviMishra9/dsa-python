from math import gcd
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        res = 2
        prod_val = 1
        start = 0
        
        for end in range(n):
            while gcd(prod_val, nums[end]) > 1:
                prod_val //= nums[start]
                start += 1
            prod_val *= nums[end]
            res = max(res, end - start + 1)
            
        return res