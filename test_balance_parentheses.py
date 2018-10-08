import unittest
from balance_parentheses import check_balance

class TestBalanceParentheses(unittest.TestCase):
    def test_balanced(self):
        self.assertTrue(check_balance("{()}{}{}({}[])"))
        self.assertTrue(check_balance(""))
        self.assertTrue(check_balance("42"))
        self.assertTrue(check_balance("{()}{21}{}({}[42])"))

    def test_unbalanced(self):
        self.assertFalse(check_balance("{()}{}{}([)]"))

