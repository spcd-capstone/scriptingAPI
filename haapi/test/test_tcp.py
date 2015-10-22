import unittest

import haapi


class TestTCPConnections(unittest.TestCase):

    def run_fake_server(self):
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1', 7777))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()

    def test_entering_with_connects(self):
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        with haapi.connect('127.0.0.1', 7777) as c:
            pass



