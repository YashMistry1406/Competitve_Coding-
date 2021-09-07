class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n= len(matrix[0])
        print(m,n)
        col = 1
        for i in range(m):
            if matrix[i][0] == 0: 
                col =0
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if matrix[i][0] ==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if col == 0:
                matrix[i][0]=0
        return matrix


'''
consider the first row and column as a flag row an column 

1)we start traversing leaving the first row and the column 
2)whenever we encounter a zero we make the corresponding element in the flag row and column as 0 
3)after the whole matrix is traversed starting from the top we now travel from backwards
4)Now we will check if any of the flag row or column has a zero in it and we would convert that whole row or column in zero 
5)we mark the flag with col = 0 or 1(true or false) so that we know that we had a zero in the flag row/column


'''