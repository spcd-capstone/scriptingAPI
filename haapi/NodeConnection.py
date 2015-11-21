import contextlib
import socket

from haapi import serialization

class NodeNotConnected(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidCommand(Exception):

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
            # Log error here
            #print("Could not connect. Exception type is {}".format(type(e).__name__))
            raise e

    def __exit__(self, type, value, traceback):
        self.sock.close()
        self.isConnected = False

    def __del__(self):
        self.sock.close()

    def setVal(self, key, value):
        if not self.isConnected:
            raise NodeNotConnected("Not connected to node ({}, {})".format(self.nodeIP, self.nodePort))
        k = serialization.serialize(key)
        v = serialization.serialize(value)
        self.sock.send(bytes("s" + k + v, 'UTF-8'))

    def getVal(self, key):
        if not self.isConnected:
            raise NodeNotConnected("Not connected to node ({}, {})".format(self.nodeIP, self.nodePort))
        k = serialization.serialize(key)
        self.sock.send(bytes("g" + k, 'UTF-8'))
        v = self.sock.recv(1024)
        return serialization.serialize(v)


