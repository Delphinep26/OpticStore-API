import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.customer import Customer, CustomerList
from resources.sale import Sale, SaleList
from resources.prescription import Prescription, PrescriptionList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True
app.secret_key = 'delphine'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Customer, '/customer/<int:_id>','/customer')
api.add_resource(CustomerList, '/customers')
api.add_resource(Sale, '/sale/<int:_id>','/sale')
api.add_resource(SaleList, '/sales')
api.add_resource(Prescription, '/prescription/<int:_id>')
api.add_resource(PrescriptionList, '/prescriptions')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)