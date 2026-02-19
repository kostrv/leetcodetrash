class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_b = 0
        right_b = len(nums) - 1
        
        while left_b <= right_b: # If we gets here, it means we have exhausted the search space and haven't found the target
            middle_index = (left_b + right_b) // 2
            current_element = nums[middle_index]

            if current_element == target: 
                # 1 Case: Successfully found the target, return the index
                return middle_index

            # Move the boundaries
            if current_element < target:
                # Element is in the right half 
                left_b = middle_index + 1
            else: 
                # Element is in the left half
                right_b = middle_index - 1

        # 2 Case: Target is not found
        # Return the left boundary value, cause it is an index of missing target place
        return left_b