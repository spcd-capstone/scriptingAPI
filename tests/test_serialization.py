import unittest

from haapi import serialization

class TestSerialization(unittest.TestCase):

    def test_serializes_int_as_str(self):
        d = serialization.serialize(1)
        self.assertTrue(isinstance(d, str))

    def test_serializes_int(self):
        d = serialization.serialize(1)
        self.assertTrue(d == "i1e")
        d = serialization.serialize(100)
        self.assertTrue(d == "i100e")

    def test_serializes_str_as_str(self):
        d = serialization.serialize("hello")
        self.assertTrue(isinstance(d, str))

    def test_serializes_str(self):
        d = serialization.serialize("hello")
        self.assertTrue(d == "5:hello")

    def test_serializes_bool_as_int(self):
        d = serialization.serialize(True)
        self.assertTrue(d == "i1e")
        d = serialization.serialize(False)
        self.assertTrue(d == "i0e")

    def test_serializing_other_raises_exception(self):
        with self.assertRaises(serialization.InvalidType):
            serialization.serialize(["one","two"])
        with self.assertRaises(serialization.InvalidType):
            serialization.serialize(1.2)

    def test_deserializing_int_returns_int(self):
        d = serialization.deserialize("i3e")
        self.assertTrue(isinstance(d, int))

    def test_deserializing_int(self):
        d = serialization.deserialize("i3e")
        self.assertTrue(d == 3)
        d = serialization.deserialize("i102e")
        self.assertTrue(d == 102)

    def test_deserializing_str_returns_str(self):
        d = serialization.deserialize("5:hello")
        self.assertTrue(isinstance(d, str))

    def test_deserializing_str(self):
        d = serialization.deserialize("5:hello")
        self.assertTrue(d == "hello")

    def test_deserializing_corrupted_raises_exception(self):
        with self.assertRaises(serialization.InvalidData):
            serialization.deserialize("ie")
        with self.assertRaises(serialization.InvalidData):
            serialization.deserialize("100:a")
        with self.assertRaises(serialization.InvalidData):
            serialization.deserialize("blah")
