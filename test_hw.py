import unittest
import hello
class TestHelloWord(unittest.TestCase):
    def test_hello(self):
        wynik = hello.zwroc()
        self.assertEqual(wynik,"Hello World")
if __name__=='__main__':
    unittest.main()
