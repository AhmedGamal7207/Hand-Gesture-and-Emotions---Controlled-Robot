from flask import Flask

app = Flask(__name__)

MESSAGE_FILE = 'message.txt'

@app.route('/')
def hi():
    return "HI"

@app.route('/robot', methods=['GET'])
def get_students():
    try:
        with open(MESSAGE_FILE, 'r') as file:
            message = file.read().strip()
        return message
    except:
        return "STOP"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
