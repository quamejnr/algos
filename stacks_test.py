import unittest
from stacks import is_valid_paranthesis, MinStack

class StackTest(unittest.TestCase):
    def test_is_valid_paranthesis(self):
        s, output = "()", True
        self.assertEqual(is_valid_paranthesis(s), output)
        s, output = "()[]{}", True
        self.assertEqual(is_valid_paranthesis(s), output)
        s, output = "[}", False
        self.assertEqual(is_valid_paranthesis(s), output)
    
    def test_stack_implementation(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.get_min(), -3)
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)
        min_stack.top() 
        self.assertEqual(min_stack.get_min(), -2)
    
if __name__ == "__main__":
    unittest.main()