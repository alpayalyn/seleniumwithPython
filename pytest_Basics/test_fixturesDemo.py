import pytest
 
@pytest.mark.usefixtures("setup")
class TestFix:
 
    def test_fixture1(self):
        print("I am the summary")
 
    def test_fixture2(self):
        print("I am the context")
 
    def test_fixture3(self):
        print("I am the appendix")
 