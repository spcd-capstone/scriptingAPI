import socket
import threading
import unittest

from multiprocessing.pool import ThreadPool

from haapi import haapi


class TestTCPConnections(unittest.TestCase):

    def run_fake_server(self):
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1', 7777))
        server_sock.listen(0)
        (conn, address) = server_sock.accept()
        conn.close()
        server_sock.close()

    def test_connection_error_raises_exception(self):
        with self.assertRaises(Exception):
            with haapi.NodeConnection('127.0.0.1', 7777):
                pass

    def test_entering_context_connects(self):
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        with haapi.NodeConnection('127.0.0.1', 7777):
            pass

        server_thread.join()

    def test_entering_context_returns_object(self):
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        with haapi.NodeConnection('127.0.0.1', 7777) as c:
            self.assertFalse(c == None)

        server_thread.join()

    def test_sending_when_not_connected_raises_NodeNotConnected(self):
        node = haapi.NodeConnection('127.0.0.1', 7777)
        with self.assertRaises(haapi.NodeNotConnected):
            node.setVal('on', 1)


if __name__ == '__main__':
    unittest.main()

