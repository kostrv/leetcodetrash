class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        current_layer = {0}
        visited = {0}
        num_coins = 0
        
        
        while current_layer:
            num_coins += 1
            next_layer = set()
            
            for total in current_layer:
                for coin in coins:
                    new_total = total + coin
                    
                    if new_total == amount:
                        return num_coins 
                    
                    if new_total < amount and new_total not in visited:
                        visited.add(new_total)
                        next_layer.add(new_total)
            
         
            current_layer = next_layer
            
        return -1 