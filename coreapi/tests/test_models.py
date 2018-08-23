import unittest
from coreapi.models import DbHandler, Question, Answer


class TestModelsDb(unittest.TestCase):

    def setUp(self):
        ''' set up variables to use for project set up '''
        print('**** setting up project ****')
        self.handler = DbHandler()
        self.answer = Answer([{'answer': 'How to get away with murder'}])
        self.question = Question('I have a bug x ', 'How do i fix bug x')
        self.dummy_data = self.handler.create(
            {'question_title': 'how do i use git', 'question_body': ' i have issues creating a PR'})

    def test_question_object(self):
        self.assertEqual(dict, type(self.question.serialize()))
        # self.assertIn({
        #     'question_title': 'I have a bug x ',
        #     'question_body': 'How do i fix bug x'
        # }, self.question.serialize())
        self.assertIn('How do i fix bug x',
                      self.question.serialize()['question_body'])

    def test_answer_object(self):
        self.assertEqual(dict, type(self.answer.serialize()))
        self.assertEqual([{'answer': 'How to get away with murder'}],
                         self.answer.serialize()['answers'])

    def test_create_question(self):
        ''' Test create question '''
        self.assertEqual('how do i use git', self.dummy_data['question_title'])
        self.assertEqual(' i have issues creating a PR',
                         self.dummy_data['question_body'])
        # self.assertEqual(2,3)

    def test_get_one_question(self):
        self.assertEqual({'_id': 1, 'question_title': 'how do i use git',
                          'question_body': ' i have issues creating a PR'}, self.handler.get(1))


if __name__ == '__main__':
    unittest.main()
