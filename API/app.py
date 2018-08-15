from flask import Flask
from flask_restplus import  Api

app = Flask(__name__, instance_relative_config=True)
# app.config.from_object('config')
# app.config.from_pyfile('config.py')
app.config['TESTING'] = True
app.config['DEBUG'] = True

api = Api(app, prefix='/api/v1', version='1.0',
          title='MiniOverFlow', description='Q and A api')


@app.route('/hello')
def welcome():
    return 'welcomde dude'