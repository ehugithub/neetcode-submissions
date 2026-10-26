class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) # num rows
        n = len(matrix[0]) # num cols
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][n-1] < target:
                top = mid + 1
                
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
            print(mid)
        
        while left <= right:
            mid2 = left + (right - left) // 2
            if matrix[mid][mid2] < target:
                left = mid2 + 1
            elif matrix[mid][mid2] > target:
                right = mid2 - 1
            else:
                return True
        return False

        