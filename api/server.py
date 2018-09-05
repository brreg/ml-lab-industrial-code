from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def predict():
    app.logger.info('Request to predict formaal: %s', request.get_json().get('formaal'))
    ## Predict based on input text
    # model.predict(theText)
    prediction = [{'industricalCode':'93.299', 'description':'Fritidsvirksomhet ellers' }]
    app.logger.info('Model predicted: %s', prediction )
    return jsonify(prediction), 200

if __name__ == '__main__':
    ## Load model using joblib
    # model = joblib.load('SVMModel.pckl')
    # Start the server
    app.run(debug=True)
