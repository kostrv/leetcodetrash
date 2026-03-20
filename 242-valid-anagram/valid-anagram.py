class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.first, self.second = {}, {}

        if len(s) != len(t):
            return False

        # for i in s:
        #     if i in self.first.keys():
        #         self.first[i] += 1 
        #     else:
        #         self.first[i] = 1

        # for i in s:
        #     if i in self.second.keys():
        #         self.second[i] += 1 
        #     else:
        #         self.second[i] = 1
        
        for i in range(len(s)):
            self.first[s[i]] = 1 + self.first.get(s[i], 0) 
            self.second[t[i]] = 1 + self.second.get(t[i], 0)

        return self.first == self.second

        # return sorted(s) == sorted(t)

