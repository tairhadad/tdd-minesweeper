# Tair Hadad - 204651897

import unittest
from minesweeper import Minesweeper
from minesweeper import GameStatus

class TestMinesweeper(unittest.TestCase):

    def createMatrix(self):
        self.minesweeper.createField(3, 4)

    def insertLayMine(self,row,col):
        self.minesweeper.layMine(row, col)

    def playTurn(self,row,col):
        self.minesweeper.play(row, col)

    def setUp(self):
        self.minesweeper = Minesweeper()
        self.createMatrix()

    def test_first_status(self):
        self.minesweeper.gameStatus = GameStatus.Playing

    def test_MatricesEqualDefault(self):
        self.assertEqual(self.minesweeper.matrix, self.minesweeper.board)

    def test_equal_matrix(self):
        self.playTurn(0,2)
        self.assertEqual(self.minesweeper.matrix, self.minesweeper.board)

    def test_createField(self):
        self.assertEqual(self.minesweeper.rows, 3)
        self.assertEqual(self.minesweeper.columns, 4)

    def test_Inserting_a_bomb(self):
        self.insertLayMine(0,0)
        self.assertEqual(self.minesweeper.board[0][0], '*')

    def test_winCheck(self):
        self.insertLayMine(0,0)
        self.playTurn(0,2)
        self.assertEqual(self.minesweeper.status(), "WIN")

    def test_Failed(self):
        self.insertLayMine(0,0)
        self.playTurn(0,0)
        self.assertEqual(self.minesweeper.status(), "LOST")

    def test_mines(self):
        self.insertLayMine(0,0)
        self.insertLayMine(0,2)
        self.assertEqual(self.minesweeper.count_mines(0,1),2)

    def test_domainCheck(self):
        self.insertLayMine(0,0)
        self.assertEqual(self.minesweeper.domainCheck(0, 0), True)
        self.assertEqual(self.minesweeper.domainCheck(2, 2), False)


if __name__ == '__main__':
    unittest.main()