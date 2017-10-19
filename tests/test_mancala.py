# test Mancala game
import pytest
import solitaire_mancala

def test_mancala_init():
    my_game = solitaire_mancala.SolitaireMancala()
    assert my_game.board == [0]