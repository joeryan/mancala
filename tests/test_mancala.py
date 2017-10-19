# test Mancala game
import pytest
import solitaire_mancala

@pytest.fixture
def game1():
    board1 = [0, 1, 1, 3, 0, 0, 0]
    my_game = solitaire_mancala.SolitaireMancala()
    my_game.set_board(board1)
    return my_game

def test_init():
    my_game = solitaire_mancala.SolitaireMancala()
    assert my_game.board == [0]

def test_configure_board():
    game = game1()
    assert str(game) == '[0, 0, 0, 3, 1, 1, 0]'

def test_valid_move_check():
    game = game1()
    assert game.is_legal_move(3)

def test_invalid_move_check():
    game = game1()
    assert not game.is_legal_move(2)

def test_get_num_seeds():
    game = game1()
    assert game.get_num_seeds(2) == 1
    assert game.get_num_seeds(3) == 3

def test_game_is_not_won():
    game = game1()
    assert not game.is_game_won()

def test_game_is_won():
    board2 = [23, 0, 0, 0, 0, 0, 0]
    my_game = solitaire_mancala.SolitaireMancala()
    my_game.set_board(board2)
    assert my_game.is_game_won()

def test_apply_move():
    pass
