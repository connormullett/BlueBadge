
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'status': 'Hello World'}), 200


@app.route('/hello')
def hello():
    return jsonify(
        {'status': 'hello Connor, ' \
            'weve been expecting you'}
    ), 200


@app.route('/hello/<name>')
def hello_name(name):
    return jsonify(
        {'status': f'hello {name}, ' \
            'weve been expecting you'}
    ), 200


if __name__ == '__main__':
    app.run(debug=True)

