class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.first = set(nums1)
        self.second = set(nums2)

        self.res = []
        for i in self.first:
            if i in self.second:
                self.res.append(i)
        
        return self.res