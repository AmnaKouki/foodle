from aziza import aziza
from monoprix import monoprix
from geant import geant
# flask

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    aziza_data = aziza(query)
    monoprix_data = monoprix(query)
    geant_data = geant(query)
    mydata = {
        'aziza': aziza_data,
        'monoprix': monoprix_data,
        'geant': geant_data,
    }
    # data = aziza_data + monoprix_data
    return jsonify(mydata)

if __name__ == '__main__':
    app.run(debug=True)

