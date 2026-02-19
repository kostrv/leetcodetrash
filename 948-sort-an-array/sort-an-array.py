from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # An array of zero or one elements is already sorted
        if len(nums) <= 1:
            return nums
        
        # For first divide we find the midpoint and split the array
        middle_index = len(nums) // 2

        # Recursively divide until we have arrays of size 1 or 0, which are inherently sorted
        left_half = self.sortArray(nums=nums[:middle_index])
        right_half = self.sortArray(nums=nums[middle_index:])
        
        # By ladder we merge the sorted halves back together
        return self.merge_parts(left_list=left_half, right_list=right_half)


    def merge_parts(self, left_list: List[int], right_list: List[int]) -> List[int]:
        # Standard merge sort logic
        result_array = []
        left_pointer = 0
        right_pointer = 0
        
        while left_pointer < len(left_list) and right_pointer < len(right_list):
            if left_list[left_pointer] <= right_list[right_pointer]:
                result_array.append(left_list[left_pointer])
                left_pointer += 1
            else:
                result_array.append(right_list[right_pointer])
                right_pointer += 1
        
        # Extend main list with leftovers
        result_array += left_list[left_pointer:]
        result_array += right_list[right_pointer:]
        
        return result_array