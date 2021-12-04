import pytest
# python -m pytest -v
@pytest.fixture()
def setup():
    print("Once before very method")
def testmethod1(setup):
    print("this is test method 1")
def testmethod2(setup):
    print("this is test method 2")

