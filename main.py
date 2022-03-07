from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:password@localhost/test', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))

    def __repr__(self):
        return f'User {self.name}'


Base.metadata.create_all(engine)


# try write a good documentation
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


@app.route('/recommendations', methods=['POST'])
def register_recommendations():
    # Get data from the POST body
    request_data = request.get_json()

    return_dict = {"example": "Register recommendations!"}

    return jsonify(return_dict)


@app.route('/teams', methods=['GET'])
def get_all_teams():
    return_dict = {"example": "'List teams!'"}

    return jsonify(return_dict)


@app.route('/recommendations', methods=['GET'])
def get_all_recommendations():
    return_dict = {"example": "List recommendations!"}

    return jsonify(return_dict)


@app.route('/recommendations/employees', methods=['GET'])
def get_all_employees_with_recommendations():
    return_dict = {"example": "List employees!"}

    return jsonify(return_dict)


if __name__ == "__main__":
    app.run(debug=True)
