import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will execute last")

def dataLoad():
    print("User profile data is being created")
    return ["Alpay", "Allen", ""]