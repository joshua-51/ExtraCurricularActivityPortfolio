from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("hey") == 20
    assert value("What's up?") == 100
