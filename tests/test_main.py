import unittest

from TryLona.main import app


class TestMain(unittest.TestCase):

    def test_app(self):
        """Dummy test."""
        self.assertEqual(app.routes[0].name, 'room')
