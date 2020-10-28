import projectcode

from projectcode.test import func, funcdouble

def test_plus():
    assert func(4) == 5

def test_double():
    assert funcdouble(4) == 8