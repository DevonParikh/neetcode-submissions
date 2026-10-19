class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)
        j = len(matrix[0])-1
        row = []
        while left < right:
            i = (left+right)//2

            if matrix[i][0] <= target <= matrix[i][j]:
                row = matrix[i]
                break
            elif target < matrix[i][0]:
                right = i
            else:
                left = i+1
        
        left, right = 0, len(row)
        while left < right:
            mid = (left+right)//2
            if target == row[mid]:
                return True
            elif target < row[mid]:
                right = mid
            else:
                left = mid + 1
        return False