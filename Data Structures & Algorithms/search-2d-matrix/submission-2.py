class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, 0
        while i + 1 < len(matrix) and matrix[i + 1][j] <= target:
            i += 1
        while j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] >= target:
                return False
            j += 1
        return False