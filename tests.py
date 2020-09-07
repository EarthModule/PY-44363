from main import foo

def test_hello():
    s = foo("im a test")
    assert s == "im a test"