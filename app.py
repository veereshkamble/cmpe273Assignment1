from flask import Flask, jsonify
from flask import request
from flask import json
from model import db
from model import TestTable
from model import app as application

from sqlalchemy.exc import IntegrityError


app = Flask(__name__)


@app.route('/v1/expenses' , methods=['POST'])
def postMethod():
    db.create_all()
    data = request.get_json(force=True)
    newUser=TestTable(data['name'], data['email'], data['category'],data['description'],
                  data['link'], data['estimated_costs'], data['submit_date'],
                  'pending', '')
    db.session.add(newUser)
    db.session.commit()

    return jsonify({'id' : newUser.id,'name' : newUser.name, 'email' : newUser.email,
                       'category' : newUser.category, 'description' : newUser.description,
                       'link' : newUser.link, 'estimated_costs' : newUser.estimated_costs,
                       'submit_date' : newUser.submit_date, 'status' : newUser.status,
                       'decision_date' : newUser.decision_date}), 201



@app.route('/v1/expenses/<int:expense_id>', methods=['GET'])
def getMethod(expense_id):
    data = TestTable.query.filter_by(id=expense_id).first_or_404()

    return jsonify({'id': data.id, 'name': data.name, 'email': data.email,
                    'category': data.category, 'description': data.description,
                    'link': data.link, 'estimated_costs': data.estimated_costs,
                    'submit_date': data.submit_date, 'status': data.status,
                    'decision_date': data.decision_date}), 200



@app.route('/v1/expenses/<int:expense_id>', methods=['PUT'])
def putMethod(expense_id):
    data = TestTable.query.filter_by(id=expense_id).first_or_404()

    newData = request.get_json(force=True)
    data.estimated_costs = newData['estimated_costs']
    db.session.commit()
    return jsonify({'status':True}), 202



@app.route('/v1/expenses/<int:expense_id>', methods=['DELETE'])
def deleteMethod(expense_id):
    data = TestTable.query.filter_by(id=expense_id).first_or_404()

    db.session.delete(data);
    db.session.commit();
    return jsonify({'status':True}), 204


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
