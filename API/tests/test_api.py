import unittest

import json

from API.app import app


class APITestCase(unittest.TestCase):
    """Unit testing class API"""

    def setUp(self):
        ''' Intial variable to use for the app '''
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client
        self.mock_data = {
            "_id": 1,
            "question": "How do i fix bug x"
        }
        self.answer = {
            'answer': 'I am answering to question 1'
        }

    def test_can_create_question(self):
        ''' Test the post request of creating a question '''
        res = self.client().post('/api/v1/questions',
                                 data=json.dumps(self.mock_data),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('1', str(res.data))

    def test_can_create_answer_to_question(self):
        ''' Test if a user can create an answer to a  question '''
        res = self.client().post('api/v1/questions/1/answers',
                                 data=json.dumps(self.answer),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_all_questions(self):
        res = self.client().post('/api/v1/questions',
                                 data=json.dumps(self.mock_data),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client().get('/api/v1/questions')
        self.assertEqual(response.status_code, 200)
        self.assertIn('How do i fix bug x', str(response.data))

    def test_can_get_one_question(self):
        res = self.client().post('/api/v1/questions',
                                 data=json.dumps(self.mock_data),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)
        response = self.client().get('/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('How do i fix bug x', str(response.data))

    def tearDown(self):
        '''teardown configs after running tests '''
        pass


if __name__ == '__main__':
    unittest.main()
