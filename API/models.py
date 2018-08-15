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
        return {"message":"question {} doesn't exist".format(_id)}