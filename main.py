from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:password@localhost/test', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Recommendation(Base):
    __tablename__ = 'recommendations'

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    employee_id = Column(Integer, ForeignKey('employees.id'))
    employee = relationship('Employee')

    def __repr__(self):
        return f'Recommendation {self.name}'


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    recommendations = relationship(Recommendation, backref='recommendation')
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship('Team')

    def __repr__(self):
        return f'Employee {self.name}'


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    employees = relationship(Employee, backref='employee')

    def __repr__(self):
        return f'Team {self.name}'


Base.metadata.create_all(engine)


@app.route('/teams', methods=['POST'])
def register_teams():
    # Get data from the POST body
    request_data = request.get_json()
    team = Team(name=request_data['name'])
    session.add(team)
    session.commit()
    session.close()

    return_dict = {"example": request_data['name']}

    return jsonify(return_dict)


@app.route('/employees', methods=['POST'])
def register_employees():
    # Get data from the POST body
    request_data = request.get_json()
    employee = Employee(name=request_data['name'], team_id=request_data['team_id'])
    session.add(employee)
    session.commit()
    session.close()

    return_dict = {"example": request_data['name']}

    return jsonify(return_dict)


@app.route('/recommendations', methods=['POST'])
def register_recommendations():
    # Get data from the POST body
    request_data = request.get_json()
    recommendation = Recommendation(name=request_data['name'], employee_id=request_data['employee_id'])
    session.add(recommendation)
    session.commit()
    session.close()

    return_dict = {"example": request_data['name']}

    #return_dict = {"example": "Register recommendations!"}

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
