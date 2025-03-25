class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        low = 0
        high = t - 1

        while low <= high :
            mid = (low+high)//2
            i = mid//n
            j = mid % n
            mid_num = matrix[i][j]
            if mid_num == target :
                return True
            elif mid_num < target :
                low = mid + 1
            else :
                high = mid - 1
        return False
            