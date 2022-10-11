import unittest
from stack import Stack, EmptyStackException, NullElementException

class TestStackLogical(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(Stack().empty(), True)
        s = Stack()
        s.push(1); self.assertEqual(s.empty(), False)
        s.pop(); self.assertEqual(s.empty(), True)

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0) 
        s.push(1)
        self.assertEqual(s.size(), 1)
        


class TrstStackRaisings(unittest.TestCase):
    def test_popfromempty(self):
        with self.assertRaises(EmptyStackException):
            Stack().pop()

    def test_pushnull(self):
        with self.assertRaises(NullElementException):
            Stack().push(None)

    def test_peekfromempty(self):
        with self.assertRaises(EmptyStackException):
            Stack().peek()



if __name__ == '__main__':
    unittest.main()
