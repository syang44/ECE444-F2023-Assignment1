import utils

def test_reversed():
    assert utils.reversed(12) == 21
    assert utils.reversed(-123) == -321
    assert utils.reversed(0) == 0
    assert utils.reversed("string") == None
    assert utils.reversed(float(12)) == None

def test_formatter():
    assert utils.formatter(12) == ('0b1100', '0o14')
    assert utils.formatter(-123) == ('-0b1111011', '-0o173')
    assert utils.formatter(0) == ('0b0', '0o0')
    assert utils.formatter("string") == None
    assert utils.formatter(2.3) == None

test_reversed()
test_formatter()