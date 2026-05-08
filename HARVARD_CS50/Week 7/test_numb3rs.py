from numb3rs import is_valid

def test_format():
    assert is_valid("1.2.3.4") == True
    assert is_valid("1.2.3") == False
    assert is_valid("1.2.3.4.5") == False

def test_range():
    assert is_valid("255.255.255.255") == True
    assert is_valid("512.1.1.1") == False
    assert is_valid("1.512.1.1") == False
    assert is_valid("1.1.512.1") == False
    assert is_valid("1.1.1.512") == False

def test_strings():
    assert is_valid("cat") == False
