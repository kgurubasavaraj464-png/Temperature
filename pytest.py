from temprature import fah
def testPostive():
    assert fah(32) == 57.6
def testZero():
    assert fah(0) == 32
def testNegative():
    assert fah(-32) == -57.6