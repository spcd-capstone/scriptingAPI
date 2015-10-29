import contextlib
import socket

@contextlib.contextmanager
def nodeConnection(nodeIP, nodePort):
    s = socket.socket()
    try:
        s.connect((nodeIP, nodePort))
        yield
    finally:
        s.close()

