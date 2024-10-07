from flask import Flask
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


app.config['SECRET_KEY'] = 'your_secret_key'

users = {
    "username": "test_user",
    "password": "test_password"
}


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    users[username] = hashed_password

    token = jwt.encode({'username': username,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=24)},
                       app.config['SECRET_KEY'])

    return jsonify({'token': token})

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users:
        return jsonify({'message': 'User does not exist'}), 400

    if not check_password_hash(users[username], password):
        return jsonify({'message': 'Invalid password'}), 400
    
    token = jwt.encode({'username': username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=24)},
                      app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token})


@app.route('/image')
def post_image():
    return 'Post Image'

@app.route('/image/{id}/transform')
def post_transform_image(id):
    return 'Post Transform Image'

@app.route('/image/{id}')
def get_image(id):
    return 'Get Image with id'

if __name__ == '__main__':
    app.run()


def test_client():
    with app.test_client() as client:
        yield client