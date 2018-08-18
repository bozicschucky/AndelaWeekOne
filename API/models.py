''' creates a db handler class to do crud operations on the API '''
from flask import abort


class DbHandler():
    ''' The oop db class to handle the db operations using oop '''

    def __init__(self):
        ''' intial variables used when forming the object '''
        self.counter = 0
        self.questions = []
        self.answers = None

    def get(self, _id):
        '''Gets the question asked provided and _id is given '''
        for question in self.questions:
            if question['_id'] == _id:
                return question
        # return (abort(404, "question {} doesn't exist".format(_id)))
        return {"message": "question {} doesn't exist".format(_id)}

    def get_all(self):
        ''' Returns all the questions stored in the data structure '''
        return self.questions

    def create(self, data):
        ''' creates the question when the data is provided '''
        question = data
        question['_id'] = self.counter = self.counter + 1
        self.questions.append(question)
        return question

    @staticmethod
    def add_items(a, l=[]):
        l.append(a)
        return l

    def answer_question(self, _id, data):
        ''' Adds an answer to the question created '''
        question = self.get(_id)
        answers = question.update({'Answers':data})
        return answers

    def delete(self, _id):
        ''' Deletes a question asked on the api '''
        question = self.get(_id)
        self.questions.remove(question)
