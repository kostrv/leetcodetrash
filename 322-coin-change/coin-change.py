class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        current_layer = {0}
        visited = {0}
        num_coins = 0
        
        # Строим уровни нашего "треугольника", пока они не закончатся
        while current_layer:
            num_coins += 1
            next_layer = set()
            
            for total in current_layer:
                for coin in coins:
                    new_total = total + coin
                    
                    if new_total == amount:
                        return num_coins # Мы достигли вершины amount!
                    
                    if new_total < amount and new_total not in visited:
                        visited.add(new_total)
                        next_layer.add(new_total)
            
            # Переходим к следующему ряду треугольника
            current_layer = next_layer
            
        return -1 # Если треугольник "закрылся", а вершину amount не нашли