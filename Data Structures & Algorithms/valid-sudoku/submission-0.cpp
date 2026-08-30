class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size() ;

        bool col[9][9] = {false};
        bool row[9][9] = {false} ;
        bool grid[9][9] = {false} ;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(board[i][j] == '.') continue ;
                int num = board[i][j] - '1' ;

                int boxidx = (i/3)*3 + (j/3) ;

                if (row[i][num] || col[j][num] || grid[boxidx][num]) {
                    return false; 
                }

                row[i][num] = col[j][num] = grid[boxidx][num] = true; 

            }
        }
        
    return true ;

    }
};
