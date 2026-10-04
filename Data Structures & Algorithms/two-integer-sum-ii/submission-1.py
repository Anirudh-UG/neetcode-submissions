class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ptr_1, ptr_2 = 0, len(numbers) - 1
        while ptr_1 < ptr_2:
            current_sum = numbers[ptr_1] + numbers[ptr_2]
            if current_sum < target:
                ptr_1 += 1
            elif current_sum > target:
                ptr_2 -= 1
            else:
                return [ptr_1 + 1, ptr_2 + 1]
        return []
        