class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Define the left and right boundaries of the search space
        left_b = 0
        right_b = len(nums) - 1
        
        while left_b <= right_b: # If we gets here, it means we have exhausted the search space and haven't found the target
            middle_index = (left_b + right_b) // 2
            current_element = nums[middle_index]

            if current_element == target: # Successfully found the target, return the index
                return middle_index

            # Move the boundaries
            if current_element < target: 
                left_b = middle_index + 1
            else: 
                right_b = middle_index - 1

        return -1