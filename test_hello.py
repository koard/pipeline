# -*- coding: utf-8 -*-
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import hello 

class TestHello(unittest.TestCase):
    def test_greet_default(self):
        self.assertEqual(hello.greet(), "Hello, world!")

    def test_greet_custom(self):
        self.assertEqual(hello.greet("Jenkins"), "Hello, Jenkins!")

    def test_main_default_prints_world_and_returns_zero(self):
        buf = io.StringIO()
        with patch.dict('os.environ', {}, clear=True):
            with redirect_stdout(buf):
                rc = hello.main()
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, world!")

    def test_main_respects_NAME_env(self):
        buf = io.StringIO()
        with patch.dict('os.environ', {'NAME': 'CI'}, clear=True):
            with redirect_stdout(buf):
                rc = hello.main()
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "Hello, CI!")

if __name__ == '__main__':
    unittest.main(verbosity=2)
