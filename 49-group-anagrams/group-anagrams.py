class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.data = {}

        for i in strs:
            key = ''.join(sorted(i))

            if key not in self.data.keys():
                self.data[key] = [i]
                continue 

            self.data[key].append(i)
        
        self.res = []
        for vals in self.data.keys():
            self.res.append(self.data[vals])

        return self.res
                    
            
        # if len(s) != len(t):
        #     return False
        
        # for i in range(len(s)):
        #     self.first[s[i]] = 1 + self.first.get(s[i], 0) 
        #     self.second[t[i]] = 1 + self.second.get(t[i], 0)


