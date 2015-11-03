import contextlib
import socket


class NodeNotConnected(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class NodeConnection:
    def __init__(self, nodeIP, nodePort):
        self.nodeIP = nodeIP
        self.nodePort = nodePort
        self.sock = socket.socket()
        self.isConnected = False

    def __enter__(self):
        try:
            self.sock.connect((self.nodeIP, self.nodePort))
            self.isConnected = True
            return self
        except Exception as e:
            print("Could not connect. Exception type is %s".format(type(e).__name__))
            raise e

    def __exit__(self, type, value, traceback):
        self.sock.close()
        self.isConnected = False

    def __del__(self):
        self.sock.close()

    def setVal(self, key, value):
        if not self.isConnected:
            raise NodeNotConnected("Never connected to node ({}, {})".format(self.nodeIP, self.nodePort))



