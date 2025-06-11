import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    message = os.getenv('APP_MESSAGE', 'Hello from Flask on AKS! (Default)')
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

