import unittest
from API.models import DbHandler


class TestModelsDb(unittest.TestCase):

    def setUp(self):
        ''' set up variables to use for project set up '''
        print('**** setting up project ****')
        self.HANDLER = DbHandler()
        print(self.HANDLER)
        self.HANDLER.create({'I am': 'Chucky'})
        self.HANDLER.create({'how': 'can i code'})
        self.HANDLER.create({'how i mer your mum': 'i am creating'})
        self.HANDLER.answer_question(1, 'i am adding an answer')


    def test_get_all_questions(self):
        self.assertEqual(3, len(self.HANDLER.get_all()))

    def test_get_one_question(self):
        self.assertEqual(
            {'_id': 3, 'how i mer your mum': 'i am creating'}, self.HANDLER.get(3))

    def test_get_question_doesnt_exit(self):
        self.assertEqual(
            ('question 6 doesn\'t exist'), self.HANDLER.get(6)['message'])

    def test_get_create_question(self):
        self.HANDLER.create({'q1': 'how to play chess'})
        self.HANDLER.create({'q2': 'create another question'})
        self.assertEqual(5, len(self.HANDLER.get_all()))

    def test_get_create_answer_question(self):
        self.HANDLER.answer_question(2, 'this is how to fix bug x')
        self.assertEqual('this is how to fix bug x',
                         self.HANDLER.get(2)['answer'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
