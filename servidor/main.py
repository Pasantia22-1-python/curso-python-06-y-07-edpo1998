from flask import Flask

app = Flask(__name__)

@app.router("/")
def hello_world():
    return 'Hola soy Erick'

if __name__ == '__main__':
    app.run()
