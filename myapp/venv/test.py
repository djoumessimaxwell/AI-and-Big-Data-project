from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

"""
cd to current directory
python test.py
export FLASK_APP=test.py
flask run
"""