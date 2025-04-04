from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"
    return jsonify({"message": "Hello, Flask!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)


#_________________________________________________________________________

from flask import Flask, request

app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user():
    if request.method == 'GET':
        return "Fetching user data"
    elif request.method == 'POST':
        return "Creating new user"
    elif request.method == 'PUT':
        return "Updating user data"
    elif request.method == 'DELETE':
        return "Deleting user"

if __name__ == '__main__':
    app.run(debug=True)


#________________________________________________________________________
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/success')
def success():
    return jsonify({"message": "Request successful"}), 200

@app.route('/not_found')
def not_found():
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)


#__________________________________________________________________________

from flask import Flask, render_template
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)


#_____________________________________________________________