import pytest
import time
import source.my_func  as my_func

def test_add():

    result = my_func.add(num1=1, num2=3)
    assert result == 4

def  test_add_strings():

    result = my_func.add(num1='i like ', num2='burgers')
    assert result == 'i like burgers'

def test_divide():

    result = my_func.divide(num1=4, num2=2)
    assert result == 2


def test_divide_zero():

    with pytest.raises(ValueError): # by this we can handle  
        my_func.divide(num1=1, num2= 0 )
    # assert True
    #here test execution is failed when assert statement is True also bcz num cannot divide by zero 
    #we can handle this 

# checking the with assert True

def test_divide_ass():

    result = my_func.divide(num1=1,  num2=1)

    assert True


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)

    result = my_func.divide(4, 2)
    assert result == 2


@pytest.mark.skip(reason='This feature is currently broken ')
def test_add():

    assert my_func.add(10, 3) == 13


@pytest.mark.xfail(reason="We cannot divide by zero")
def test_divide_zero_broken():

    my_func.divide(4, 0)