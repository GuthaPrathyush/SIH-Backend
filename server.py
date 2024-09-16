from flask import Flask, request
from get_response import load_and_get_district_data
from flask_cors import CORS

app = Flask('__name__')
CORS(app=app, origin='*', methods=['GET', 'POST'])

@app.route('/getresponse', methods=['POST'])
def getresponse():
    csv_file = 'ap_groud_waterf.csv'
    if request.method == 'POST':
        data = request.json
        district = data.get('district') if data else ''
    else:
        return 'Error route not found'

    return load_and_get_district_data(csv_file=csv_file, district_name=district)


if __name__ == "__main__":
    app.run(debug=True)
