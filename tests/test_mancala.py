# test Mancala game
import pytest
import solitaire_mancala

def test_init():
    my_game = solitaire_mancala.SolitaireMancala()
    assert my_game.board == [0]

def test_configure_board():
    board1 = [0, 1, 1, 3, 0, 0, 0]
    my_game = solitaire_mancala.SolitaireMancala()
    my_game.set_board(board1)
    assert str(my_game) == '[0, 0, 0, 3, 1, 1, 0]'

def test_valid_move_check():
    board1 = [0, 1, 1, 3, 0, 0, 0]
    my_game = solitaire_mancala.SolitaireMancala()
    my_game.set_board(board1)
    assert my_game.is_legal_move(3)

def test_invalid_move_check():
    board1 = [0, 1, 1, 3, 0, 0, 0]
    my_game = solitaire_mancala.SolitaireMancala()
    my_game.set_board(board1)
    assert not my_game.is_legal_move(2)

def test_get_num_seeds():
    board1 = [0, 1, 1, 3, 0, 0, 0]
    my_game = solitaire_mancala.SolitaireMancala()
    my_game.set_board(board1)
    assert my_game.get_num_seeds(2) == 1
    assert my_game.get_num_seeds(3) == 3