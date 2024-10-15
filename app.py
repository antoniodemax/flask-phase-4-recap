from flask import Flask, make_response
from flask_migrate import Migrate
from models import *



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/users')
def users():
    response = [user.to_dict() for user in User.query.all()]

    # users = User.query.all()

    # print(users)
    return make_response(response, 200)


@app.route('/')
def index():
    return 'Welcome to flask!'

if __name__ == '__main__':
    app.run(port=8080, debug=True)