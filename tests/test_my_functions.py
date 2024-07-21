import pytest

import source.my_func  as my_func


def test_add():

    result = my_func.add(num1=1, num2=3)
    assert result == 4

def test_divide():

    result = my_func.divide(num1=4, num2=2)
    assert result == 2.1