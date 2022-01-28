from flask import Flask, jsonify, request

app = Flask(__name__)
app.run(debug=True)


@app.route('/teams', methods=['POST'])
def register_teams():
    # Get data from the POST body
    request_data = request.get_json()

    return_dict = {"example": "Register teams!"}

    return jsonify(return_dict)


@app.route('/employees', methods=['POST'])
def register_employees():
    # Get data from the POST body
    request_data = request.get_json()

    return_dict = {"example": "Register employees!"}

    return jsonify(return_dict)


@app.route('/referrals', methods=['POST'])
def register_referrals():
    # Get data from the POST body
    request_data = request.get_json()

    return_dict = {"example": "Register referrals!"}

    return jsonify(return_dict)


@app.route('/teams', methods=['GET'])
def get_all_teams():
    return_dict = {"example": "'List teams!'"}

    return jsonify(return_dict)


@app.route('/referrals', methods=['GET'])
def get_all_referrals():
    return_dict = {"example": "List referrals!"}

    return jsonify(return_dict)


@app.route('/referrals/employees', methods=['GET'])
def get_all_referrals_employees():
    return_dict = {"example": "List employees!"}

    return jsonify(return_dict)
