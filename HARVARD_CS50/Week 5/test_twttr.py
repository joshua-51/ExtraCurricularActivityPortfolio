from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("1234") == "1234"
    assert shorten(".,!?") == ".,!?"
