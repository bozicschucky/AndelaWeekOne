import unittest

import json

from API import app


class APITestCase(unittest.TestCase):
    """Unit testing class API"""

    def setUp(self):
        ''' Intial variable to use for the app '''
        self.app = app
        self.client = self.app.test_client
        self.mock_data = {
            "_id": 0,
            "question": "How do i fix bug x"
        }