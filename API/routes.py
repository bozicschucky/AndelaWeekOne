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


