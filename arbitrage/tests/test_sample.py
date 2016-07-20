from context import exchange

import unittest
import requests

class BasicTestSuite(unittest.TestCase):
    def test_hmm(self):
    	msg = exchange.sample_say()
        assert "hello" in msg

if __name__ == '__main__':
    unittest.main()
