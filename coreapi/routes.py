''' routes file to handle all api routes '''

from flask_restplus import Resource, fields
from .app import api
from .models import DbHandler

handler = DbHandler()


question = api.model('Question', {
    '_id': fields.Integer(readOnly=True,
                          description='Question id'),
    'question_title': fields.String(required=True,
                                    description='The question title', min_length=10),

    'question_body': fields.String(required=True,
                                   description='The question details', min_length=10)
})

answer = api.model('Answer', {
    'Answer_title': fields.String(required=True,
                                  description='The Answer title', min_length=10),
    'Answer_body': fields.String(required=True,
                                 description='The Answer details', min_length=10)
})


@api.route('/questions')
class AllQuestions(Resource):
    """Get and create questions as specified"""

    def get(self):
        """Get all questions asked """
        questions = handler.get_all()
        return questions

    @api.expect(question, validate=True)
    @api.marshal_with(question, skip_none=True, code=201)
    def post(self):
        """ Create a specific question """
        data = api.payload
        return handler.create(data), 201


@api.route('/questions/<int:_id>')
class Question(Resource):
    """Shows single items of the resources created"""

    def get(self, _id):
        ''' Get a given resource/question based on id '''
        return handler.get(_id)

    def delete(self, _id):
        '''Delete a certain resource/question given an id'''
        handler.delete(_id)
        return {'message': 'question {} deleted'.format(_id)}, 204


@api.route('/questions/<int:_id>/answers')
class QuestionsReply(Resource):
    """Reply to a specific question"""
    @api.expect(answer, validate=True)
    @api.marshal_with(answer, skip_none=True, code=201)
    def post(self, _id):
        '''Get a question and reply to it with an Answer '''
        # data = handler.add_items(api.payload)
        data = api.payload
        handler.answer_question(_id, data)
        return {'message': 'answer created for  question {}'.format(_id)}, 201
