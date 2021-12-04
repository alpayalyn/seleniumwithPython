import pytest

@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

def test_fixture(setup):
    print("I will follow the steps")