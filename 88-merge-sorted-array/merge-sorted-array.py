class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # For readability
        size1 = m 
        size2 = n 
                
        result_array = []
        left_pointer = 0
        right_pointer = 0

        # Compare elements from the start of both arrays
        while left_pointer < size1 and right_pointer < size2: # Loop until we reach the end of either array
            if nums1[left_pointer] <= nums2[right_pointer]:
                result_array.append(nums1[left_pointer])
                left_pointer += 1
            else:
                result_array.append(nums2[right_pointer])
                right_pointer += 1

        # while left_pointer < size1:
        #     result_array.append(nums1[left_pointer])
        #     left_pointer += 1

        # while right_pointer < size2:
        #     result_array.append(nums2[right_pointer])
        #     right_pointer += 1

        # Leftovers managment
        if left_pointer < size1:
            result_array += nums1[left_pointer:size1] 
        
        if right_pointer < size2:
            result_array += nums2[right_pointer:size2] 

        # Replace the elements in nums1 with the sorted result as a requirement to pass
        for index in range(size1 + size2):
            nums1[index] = result_array[index]