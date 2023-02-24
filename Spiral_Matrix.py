'''Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10'''

#Expected Time Complexity: O(N*M)
#Expected Auxiliary Space: O(N*M)

def spirallyTraverse(self,matrix, r, c): 
        top = 0
        down = r-1
        left = 0
        right = c-1
        
        dir = 0 # 0-right,1-down,2-left,3-top
        ans = []
        
        while top<=down and left<=right:
            if dir==0:
                for i in range(left,right+1):
                    ans.append(matrix[top][i])
                top+=1
            if dir==1:
                for i in range(top,down+1):
                    ans.append(matrix[i][right])
                right-=1
            if dir==2:
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
                down-=1
            if dir==3:
                for i in range(down,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
            dir = (dir+1) % 4
        
        return ans
