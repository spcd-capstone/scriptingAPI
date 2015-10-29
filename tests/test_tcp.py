import socket
import threading
import unittest

from haapi import haapi


class TestTCPConnections(unittest.TestCase):

    def run_fake_server(self):
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1', 7777))
        server_sock.listen(0)
        (conn, address) = server_sock.accept()
        conn.close()
        server_sock.close()

    def test_entering_with_connects(self):
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        with haapi.nodeConnection('127.0.0.1', 7777):
            pass

        server_thread.join()


if __name__ == '__main__':
    unittest.main()

