class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        pivot, ptr_1, ptr_2 = 0, 0, len(nums) - 1
        total_length = len(nums)
        result = []

        while pivot < total_length:
            target_sum = 0 - nums[pivot]

            # to remove duplicate entries
            if ptr_1 == pivot:
                ptr_1 += 1
            if ptr_2 == pivot:
                ptr_2 -=1

            while ptr_1 < ptr_2:
                current_sum = nums[ptr_1] + nums[ptr_2]
                if current_sum < target_sum:
                    ptr_1 += 1
                elif current_sum > target_sum:
                    ptr_2 -= 1

                else:
                    if ptr_1 != ptr_2:
                        triplet = [nums[pivot], nums[ptr_1],nums[ptr_2]]
                        triplet.sort()
                        if triplet not in result:
                            result.append(triplet)
                    ptr_1 += 1
                    ptr_2 -= 1
            pivot += 1
            ptr_1, ptr_2 = pivot + 1, len(nums) - 1
        return result 
        