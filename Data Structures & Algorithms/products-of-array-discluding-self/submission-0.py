import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_no_zero = [item for item in nums if item != 0]
        nums_all_zero = [item for item in nums if item == 0]
        
        if not nums_no_zero or len(nums_all_zero) > 1:
            return [0]*len(nums)

        total_prod_zero = math.prod(nums_no_zero)

        total_prod = math.prod(nums)

        return [total_prod//num if num != 0 else total_prod_zero for num in nums]