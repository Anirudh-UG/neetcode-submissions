class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        set_of_nums = set(nums)

        for idx in range(len(nums)):
            ele = target - nums[idx]
            if ele in set_of_nums and nums.index(ele) != idx:
                return sorted([idx,nums.index(ele)])
        