from flask import Flask, render_template, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_attendance', methods=['POST'])
def add_attendance():
    data = request.json

    block = blockchain.create_block(data=data)

    return jsonify({
        'message': 'Attendance recorded',
        'block': block
    }), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain.chain)

if __name__ == '__main__':
    app.run(debug=True)