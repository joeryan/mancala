# test Mancala game
import pytest
import solitaire_mancala

def test_mancala_init():
    my_game = solitaire_mancala.SolitaireMancala()
    assert my_game.board == [0]

def test_mancala_configure_board():
    board = [0, 1, 1, 3, 0, 0, 0]
    my_game = solitaire_mancala.SolitaireMancala()
    my_game.set_board(board)
    assert str(my_game) == '[0, 1, 1, 3, 0, 0, 0]'