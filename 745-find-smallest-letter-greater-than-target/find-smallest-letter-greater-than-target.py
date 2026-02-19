class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left_boundary = 0
        right_boundary = len(letters) - 1
        
        # If target is greater than or equal to the last letter,
        # wrap around and return the first letter as per the problem rules.
        if target >= letters[right_boundary]:
            return letters[0]

        while left_boundary <= right_boundary:
            middle_index = (left_boundary + right_boundary) // 2
            current_char = letters[middle_index]
            
            if current_char <= target:
                # If current char is not greater than target, search in the right half.
                left_boundary = middle_index + 1
            else:
                # If current char is greater, it could be our answer, 
                # but we keep searching left to find the smallest possible greater char.
                right_boundary = middle_index - 1
                
        # After the loop, left_boundary points to the smallest char strictly greater than target.
        return letters[left_boundary]