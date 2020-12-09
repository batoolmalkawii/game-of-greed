from game_of_greed import __version__
from tests.flow.flo import Flo

def test_version():
    assert __version__ == '0.1.0'

def test_quitter():
    Flo.test('tests/flow/quitter.txt')

def test_wanna_play_yes_then_quit():
    Flo.test('tests/flow/do_wanna_play_then_quit.txt')

def test_zilch():
    Flo.test('tests/flow/zilch.txt')

def test_hot_dice():
    Flo.test('tests/flow/hot_dice.txt')



def test_bank_one_roll_then_quit():
    Flo.test('tests/flow/bank_one_roll_then_quit.txt')


def test_bank_first_for_two_rounds():
    Flo.test('tests/flow/bank_first_for_two_rounds.txt')

