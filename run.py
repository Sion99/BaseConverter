from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['POST'])
def convertbase():

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
