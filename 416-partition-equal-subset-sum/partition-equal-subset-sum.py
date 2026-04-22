class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        reachable = {0}
        
        for num in nums:
            next_reachable = set()
            
            for current_sum in reachable:
                new_sum = current_sum + num
                
                if new_sum == target:
                    return True  
                
                if new_sum < target:
                    next_reachable.add(new_sum)
            
            # объединяем старые суммы с новыми 
            reachable = reachable | next_reachable
        
        return False