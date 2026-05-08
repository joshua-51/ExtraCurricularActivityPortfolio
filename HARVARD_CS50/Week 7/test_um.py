from um import count

def test_isolated():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_case():
    assert count("UM, UM, UM") == 3
    assert count("um Um uM") == 3

def test_inside_word():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("instrumentation") == 0
