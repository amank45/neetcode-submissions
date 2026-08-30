class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [[False]*9 for _ in range(9)] 
        col = [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue 

                num = int(board[i][j]) - 1 
                bidx = (i//3)*3 + (j//3) 

                if col[i][num] or row[j][num] or box[bidx][num]:
                    return False 
                
                col[i][num] = row[j][num] = box[bidx][num] = True 

        return True ;

        
        