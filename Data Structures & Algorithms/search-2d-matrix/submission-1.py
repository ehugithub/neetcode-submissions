class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m
        rowNum = 0

        while low < high:
            mid = low + (high - low) // 2
            if target < matrix[mid][0]:
                high = mid
            elif target > matrix[mid][n - 1]:
                low = mid + 1
            else:
                rowNum = mid
                break
        if low >= high: return False
        row = matrix[rowNum]
        # binary search
        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            if target < row[mid]:
                right = mid
            elif target > row[mid]:
                left = mid + 1
            else:
                return True                        

        return False
            
