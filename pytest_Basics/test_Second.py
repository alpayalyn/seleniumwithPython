import pytest

@pytest.mark.smoke
def test_SecondProgram():
    msg = "Alpay"
    assert msg == "Alpay", "Test is Failed. Because string doesnt match"
    print("NO")