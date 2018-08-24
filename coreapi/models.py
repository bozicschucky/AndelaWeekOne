''' creates a db handler class to do crud operations on the API '''


class Question():
    ''' Question class '''
    idCounter = 0

    def __init__(self, title, body):
        ''' intiate default values for the class '''
        self.title = title
        self.body = body
        Question.idCounter += 1

    def serialize(self):
        ''' return json representation of the class '''
        question = {
            '_id': Question.idCounter,
            'question_title': self.title,
            'question_body': self.body
        }
        return question


class Answer():
    ''' Answer class '''

    def __init__(self, title,body):
        ''' instantiate Answer object '''
        self.title = title
        self.body = body 
        

    def serialize(self):
        ''' return json represenatation of the object '''
        answer = {
            'answer_title': self.title,
            'answer_body': self.body,
        }
        return answer



class DbHandler(Question, Answer):
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
        question_object = Question
        data = question_object(data['question_title'], data['question_body'])
        question = data.serialize()
        question['_id'] = self.counter = self.counter + 1
        self.questions.append(question)
        return question

    def add_items(self, a, l=[]):
        l.append(a)
        return l

    def answer_question(self, _id, data):
        ''' Adds an answer to the question created '''
        answer_object = Answer(data['Answer_title'],data['Answer_body'])
        question = self.get(_id)
        answer = answer_object.serialize()
        answers = self.add_items(answer)
        answers = question.update({'Answer': answer})
        return answers

    def delete(self, _id):
        ''' Deletes a question asked on the api '''
        question = self.get(_id)
        self.questions.remove(question)
