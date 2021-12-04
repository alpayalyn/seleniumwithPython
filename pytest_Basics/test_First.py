# Any PyTest file should start with test_ or end with _test
# PtTest method names should start with "test"
#Any code should be wrapped in method only
# Method name shoud have sense
# -k stands for method names execution, -s logs in output -v stands for more info metadata
# You can run specific file with py.test <filename>
# if you get stuck right click then comman palette write test, and go to py.test

import unittest

def test_firstProgram():
    msg = "Alpay"
    assert msg == "Alpay", "Test is Failed. Because string doesnt match"
    print("hi")
