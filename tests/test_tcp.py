import socket
import threading
import unittest

from multiprocessing.pool import ThreadPool
from time import sleep

from haapi import NodeConnection
import haapi


class TestTCPConnections(unittest.TestCase):

    # A fake server which mimics a node. To be run in a seperate process.
    # will pass messages to multiprocessor. Queue parameter
    def run_fake_server(self, q = None):
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1', 7777))
        server_sock.listen(0)
        (conn, address) = server_sock.accept()
        sleep(0.1)
        conn.close()
        server_sock.close()

    def test_connection_error_raises_exception(self):
        with self.assertRaises(Exception):
            with NodeConnection('127.0.0.1', 7777):
                pass

    def test_entering_context_connects(self):
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        with NodeConnection('127.0.0.1', 7777):
            pass

        server_thread.join()

    def test_entering_context_returns_object(self):
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        with NodeConnection('127.0.0.1', 7777) as c:
            self.assertFalse(c == None)

        server_thread.join()

    def test_sending_when_not_connected_raises_NodeNotConnected(self):
        node = NodeConnection('127.0.0.1', 7777)
        with self.assertRaises(haapi.NodeNotConnected):
            node.setVal('on', 1)

    def test_getting_when_not_connected_raises_NodeNotConnected(self):
        node = NodeConnection('127.0.0.1', 7777)
        with self.assertRaises(haapi.NodeNotConnected):
            node.getVal('on')


if __name__ == '__main__':
    unittest.main()

