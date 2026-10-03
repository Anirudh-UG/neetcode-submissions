class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        
        res = [0] * len(nums)
        if zero_cnt > 1: return res

        for idx, c in enumerate(nums):
            if zero_cnt:
                res[idx] = 0 if c else prod
            else:
                res[idx] = prod // c
        return res
        
