class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.vals = {}

        for i in nums:
            if i in self.vals.keys():
                self.vals[i] += 1 
                return True
            else:
                self.vals[i] = 1
        
        return False

        # self.vals = []

        # for i in nums:
        #     if i in self.vals:
        #         return True
        #     else:
        #         self.vals.append(i)
        
        # return False