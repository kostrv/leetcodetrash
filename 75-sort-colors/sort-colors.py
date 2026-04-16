class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            el = nums[i]
            compare = i - 1

            while compare >= 0 and el < nums[compare]:
                nums[compare + 1] = nums[compare]
                compare -= 1

            nums[compare + 1] = el
         