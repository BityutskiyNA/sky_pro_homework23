from flask import Flask, request, jsonify
from marshmallow import ValidationError

from model import RequestParams
from qwery import build_query

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        params = RequestParams().load(request.json)
    except ValidationError as error:
        return error.messages, 400
    result = build_query(cmd1=params['cmd1'],cmd2=params['cmd2'], param1=params['value1'], param2=params['value2'])
    return jsonify(result)

if __name__ == '__main__':
    app.run()
