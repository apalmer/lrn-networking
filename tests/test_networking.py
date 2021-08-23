from networking import hello
import networking

def test_hello():
    greeting = networking.hello()
    assert greeting == "hello"