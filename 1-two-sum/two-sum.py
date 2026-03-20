class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.values = {}

        for id, num in enumerate(nums):
            diff = target - num

            if diff in self.values: 
                return [self.values[diff], id]
            self.values[num] = id