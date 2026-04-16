import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # for i in range(len(nums)):
        #     el = nums[i]
        #     compare = i - 1

        #     while compare >= 0 and el > nums[compare]:
        #         nums[compare + 1] = nums[compare]
        #         compare -= 1

        #     nums[compare+1] = el  

        # result = []
        # for i in range(len(nums)):
        #     el = nums[i]
        #     count = 0
            
        #     for item in nums[i+1:][::-1]:
        #         if item < el: 
        #             count += 1
            
        #     result.append(count)
        
        # return result


        result = []
        sorted_list = []
        
        # Идем с конца в начало
        for i in range(len(nums) - 1, -1, -1):
            # Находим индекс, куда бы мы вставили nums[i] в отсортированный список
            # bisect_left вернет количество элементов, которые строго меньше nums[i]
            idx = bisect.bisect_left(sorted_list, nums[i])
            result.append(idx)
            # Вставляем элемент, сохраняя порядок (это O(n), но в Python работает быстро)
            sorted_list.insert(idx, nums[i])
            
        return result[::-1] # Разворачиваем результат обратно