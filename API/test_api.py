import unittest

import json

from API import app
from API.models import DbHandler


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

    def test_can_create_question(self):
        ''' Test the post request of creating a question '''
        res = self.client().post('/api/v1/questions',
                                 data=json.dumps(self.mock_data),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('How do i fix bug x', str(res.data))