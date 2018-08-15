from flask_restplus import Resource, fields
from .app import api, app
from .models import DbHandler

HANDLER = DbHandler()

QUESTION = api.model('Question', {
                     '_id': fields.Integer(readOnly=True, description='Question id'),
                     'question': fields.String(required=True,
                                               description='The question details')
                     })

ANSWER = api.model('Answer', {
    'Answer': fields.String(required=True, description='The Answer details')
})


@api.route('/questions')
class AllQuestions(Resource):
    """Get and create questions as specified"""

    def get(self):
        """Get all questions asked """
        questions = HANDLER.get_all()
        return questions

    @api.expect(QUESTION)
    def post(self):
        """ Create a specific question """
        return HANDLER.create(api.payload), 200


@api.route('/questions/<int:_id>')
class Question(Resource):
    """Shows single items of the resources created"""

    def get(self, _id):
        ''' Get a given resource/question based on id '''
        return HANDLER.get(_id)

    def delete(self, _id):
        '''Delete a certain resource/question given an id'''
        return HANDLER.delete(_id)


@api.route('/questions/<int:_id>/answers')
class QuestionsReply(Resource):
    """Reply to a specific question"""
    @api.expect(ANSWER)
    def post(self, _id):
        '''Get a question and reply to it with an Answer '''
        return HANDLER.answer_question(_id, api.payload), 200
