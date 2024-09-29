from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


a = 4
b = "four"
c = True
d = 2.3

if __name__ == '__main__':
    app.run()
