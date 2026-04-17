class Solution:
    def rob(self, nums: List[int]) -> int:
        count = len(nums)

        if count == 0: return 0
        if count == 1: return nums[0]

        amounts = [0] * count
        
        amounts[0] = nums[0]
        amounts[1] = max(nums[1], nums[0])

        for i in range(2, count):
            previous = amounts[i-1]
            current_and_previous = nums[i] + amounts[i-2]
            amounts[i] = max(previous, current_and_previous)

        return amounts[-1]
        