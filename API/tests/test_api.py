import unittest

import json

from API.app import app
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

    def test_get_all_questions(self):
        res = self.client().post('/api/v1/questions',
                                 data=json.dumps(self.mock_data),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)
        response = self.client().get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)
        self.assertIn('How do i fix bug x', str(response.data))

    def test_can_get_one_question(self):
        res = self.client().post('/api/v1/questions',
                                 data=json.dumps(self.mock_data),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)
        response = self.client().get('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('How do i fix bug x', str(response.data))

    # def test_fail_when_wrong_id_passed(self):
    #     response = self.client().get('/api/v1/questions/40')
    #     self.assertEqual(response.status_code, 404)
        # self.assertIn('question 40 doesnt exist', str(response.data[4]))

    def tearDown(self):
        '''teardown configs after running tests '''
        pass


if __name__ == '__main__':
    unittest.main()