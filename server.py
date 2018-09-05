from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def predict():
    data = [{'industrical code':'93.299', 'description':'Fritidsvirksomhet ellers' }]
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
