from flask import Flask

app = Flask(__name__)


@app.get('/')
@app.get('/index')
def index():
    return 'OMG'
