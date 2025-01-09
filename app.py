from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    # Ensure it's listening on 0.0.0.0 for Docker to access it
    app.run(host='0.0.0.0', port=5000)