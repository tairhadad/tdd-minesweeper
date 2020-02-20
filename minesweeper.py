# Tair Hadad - 204651897

import copy
from enum import Enum
class GameStatus(Enum):
    Win = "WIN"
    Lost = "LOST"
    Playing = "PLAYING"

class Minesweeper:
    def __init__(self):
        self.rows = 1
        self.columns = 1
        self.matrix = []
        self.board = []
        self.gameStatus = GameStatus.Playing

    def status(self):
        return self.gameStatus.value

    def createField(self, rows: object, columns: object) -> object:
        self.rows = rows
        self.columns = columns
        self.matrix = [['.' for _ in range(columns)] for _ in range(rows)]
        self.board = copy.deepcopy(self.matrix)

    def winCheck(self):
        flag=True
        while (flag):
            for i in range(self.rows):
                for j in range(self.columns):
                    if (self.matrix[i][j] == self.board[i][j] and self.board[i][j] !='.'):
                        continue
                    elif(self.matrix[i][j]=='.' and self.board[i][j] =='*'):
                        continue
                    else:
                        flag=False
                        return
            if(flag and (self.gameStatus != GameStatus.Lost)):
                self.gameStatus = GameStatus.Win
                break
            return

    def layMine(self, row, columns):
        self.board[row][columns] = '*'

    def printField(self):
        if(self.gameStatus.value == "PLAYING"):
            for i in range(self.rows):
                print('"', end='')
                for j in range(self.columns):
                    print(self.matrix[i][j], end=' ')
                print('"')
            print()
        else:
            for i in range(self.rows):
                print('"', end='')
                for j in range(self.columns):
                    print(self.board[i][j], end=' ')
                print('"')
            print()

    def domainCheck(self,row,col):
        if row<self.rows and row >=0 and col>=0 and col<self.columns:
            if self.board[row][col] == '*':
                return True
        return False

    def count_mines(self,a, b):
        count = 0
        try:
            if (self.domainCheck(a - 1,b - 1)): count += 1
            if (self.domainCheck(a + 0,b - 1)):count += 1
            if (self.domainCheck(a + 1,b - 1)):count += 1
            if (self.domainCheck(a - 1,b + 0)):count += 1
            if (self.domainCheck(a + 1,b + 0)):count += 1
            if (self.domainCheck(a - 1,b + 1)):count += 1
            if (self.domainCheck(a + 0,b + 1)):count += 1
            if (self.domainCheck(a + 1,b + 1)):count += 1
        except IndexError:
            temp = 'The selected location does not exist'
            print(temp)
        return count

    def play(self,row,col):
        try:
            if self.you_Lose(col, row):
                self.gameStatus = GameStatus.Lost
            else:
                if self.matrix[row][col] == '.':
                    count = self.count_mines(row, col)
                    if self.count_Not_Zero(col, count, row):
                        self.winCheck()
                    elif self.not_Bomb(col, row):
                        self.flood_Fill(col, row)
                        self.winCheck()
        except IndexError:
            temp = 'The selected location does not exist'
            print(temp)

    def flood_Fill(self, col, row):
        if (row > 0):
            self.play(row - 1, col)
        if (row < len(self.matrix) - 1):
            self.play(row + 1, col)
        if (col > 0):
            self.play(row, col - 1)
        if (col < len(self.matrix[row]) - 1):
            self.play(row, col + 1)

    def not_Bomb(self, col, row):
        if self.board[row][col] != '*':
            self.matrix[row][col] = '+'
            self.board[row][col] = '+'
            return True
        return False

    def count_Not_Zero(self, col, count, row):
        if (count > 0):
            self.matrix[row][col] = str(count)
            self.board[row][col] = str(count)
            return True
        return False

    def you_Lose(self, col, row):
        if self.board[row][col] == '*':
            self.matrix[row][col] = '*'
            return True
        return False
