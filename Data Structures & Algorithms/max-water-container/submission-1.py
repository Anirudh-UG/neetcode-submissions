class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left_ptr, right_ptr = 0, len(heights) - 1
        while left_ptr < right_ptr:
            current_area = abs(left_ptr - right_ptr) * min(heights[left_ptr],heights[right_ptr])
            if max_area < current_area:
                max_area = current_area
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            elif heights[left_ptr] > heights[right_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
        return max_area
        