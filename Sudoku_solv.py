class Solution:
    def solveSudoku(self, board:list) -> None:
        self.board = board

    cifri = [1,2,3,4,5,6,7,8,9]

    def valid_not_valid(self):
        for i in range(len(self.board)):
            for t in range(len(self.board[i])):
                if self.board[i].count(f"{t+1}") > 1:
                    print("False")
                    return False
        for i in range(len(self.board)):
            temp1 = []
            for t in range(len(self.board[i])):
                temp1.append(self.board[t][i])
            for x in range(len(temp1)):
                if temp1.count(f"{x+1}") > 1:
                    print("False")
                    return False
                
        for i in range(3):
            # temp2 = [board[i+2*i][0:3],board[i+1+2*i][0:3],board[i+2+2*i][0:3]]
            temp2 = []
            temp2.extend(self.board[i+2*i][0:3])
            temp2.extend(self.board[i+1+2*i][0:3])
            temp2.extend(self.board[i+2+2*i][0:3])
            temp3 = []
            temp3.extend(self.board[i+2*i][3:6])
            temp3.extend(self.board[i+1+2*i][3:6])
            temp3.extend(self.board[i+2+2*i][3:6])
            temp4 = []
            temp4.extend(self.board[i+2*i][6:9])
            temp4.extend(self.board[i+1+2*i][6:9])
            temp4.extend(self.board[i+2+2*i][6:9])
            for x in range(len(temp1)):
                if temp2.count(f"{x+1}") > 1 or temp3.count(f"{x+1}") > 1 or temp4.count(f"{x+1}") > 1:
                    print("False")
                    return False
        return True

    adfa














aga = Solution()
aga.board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(aga.valid_not_valid())