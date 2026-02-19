class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_b = 0
        right_b = len(nums) - 1
        
        while left_b <= right_b:
            middle_index = (left_b + right_b) // 2
            current_element = nums[middle_index]

            if current_element == target:
                return middle_index

            if current_element < target:
                left_b = middle_index + 1
            else: 
                right_b = middle_index - 1

        return -1