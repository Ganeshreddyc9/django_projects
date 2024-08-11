# django_projects
web_app projects 

use of conftest.py file 

we can make our fixures global so that we can use every where u want 


@pytest.fixture
def my_rectangle():

    return shapes.Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():

    return shapes.Rectangle(5, 6)


my_rectangle, weird_rectangle are in use 
these are related to test_rectangle.py so that they are working fine 