import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.resources.user import UserRegister, User, UserLogin
from src.resources.customer import Customer, CustomerList
from src.resources.sale import Sale, SaleList
from src.resources.prescription import Prescription, PrescriptionList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True
app.secret_key = 'delphine'
api = Api(app)


jwt = JWTManager(app)
"""
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below.
"""


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1:
        return {'is_admin': True}
    return {'is_admin': False}


api.add_resource(Customer, '/customer/<int:_id>','/customer')
api.add_resource(CustomerList, '/customers')
api.add_resource(Sale, '/sale/<int:_id>','/sale')
api.add_resource(SaleList, '/sales')
api.add_resource(Prescription, '/prescription/<int:_id>','/prescription')
api.add_resource(PrescriptionList, '/prescriptions')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)