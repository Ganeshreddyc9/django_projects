import pytest 

import source.shapes as shapes


def test_area(my_rectangle):

    assert my_rectangle.area() == 10 *20


def test_perimeter(my_rectangle):

    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)
 

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle != weird_rectangle 






# def test_area():

#     rectangle = shapes.Rectangle(10, 20)

#     assert rectangle.area() == 10 *20


# def test_perimeter():

#     rectangle = shapes.Rectangle(10, 20)

    # assert rectangle.perimeter() == (10 * 2) + (20 * 2)

#  rectangle = shapes.Rectangle(10, 20)

# here the rectangle method is used as a multiple conditions and that where that fixure come in to picture c