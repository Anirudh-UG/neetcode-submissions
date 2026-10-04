class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        total_length = len(nums)
        result = []

        for pivot in range(total_length - 2):
            if nums[pivot] > 0:
                break

            # 1. Skip duplicate values for the pivot
            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue

            target_sum = -nums[pivot]
            ptr_1 = pivot + 1
            ptr_2 = total_length - 1

            while ptr_1 < ptr_2:
                current_sum = nums[ptr_1] + nums[ptr_2]

                if current_sum < target_sum:
                    ptr_1 += 1
                elif current_sum > target_sum:
                    ptr_2 -= 1
                else:
                    # Valid triplet found
                    result.append([nums[pivot], nums[ptr_1], nums[ptr_2]])

                    # Skip duplicate values for both pointers
                    while ptr_1 < ptr_2 and nums[ptr_1] == nums[ptr_1 + 1]:
                        ptr_1 += 1
                    while ptr_1 < ptr_2 and nums[ptr_2] == nums[ptr_2 - 1]:
                        ptr_2 -= 1

                    # Move past the last checked values
                    ptr_1 += 1
                    ptr_2 -= 1

        return result