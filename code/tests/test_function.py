import projectcode

from projectcode.test import func, funcdouble

def test_plus():
    assert func(4) == 5

def test_double():
    assert funcdouble(4) == 8


def test_calculate(mocker):
    num = 5
    mock_move_blob_file = mocker.patch('projectcode.test.funcdouble')
    mock_move_blob_file.return_value = 10
    projectcode.test.funccalculate(num)
    assert mock_move_blob_file.called