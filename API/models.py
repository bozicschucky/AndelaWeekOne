''' creates a db handler class to do crud operations on the API '''
from flask import abort



class DbHandler():
    ''' The oop db class to handle the db operations using oop '''

    def __init__(self):
        ''' intial variables used when forming the object '''
        self.counter = 0
        self.questions = []
        self.answers = None