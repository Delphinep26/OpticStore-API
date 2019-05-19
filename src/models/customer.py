
from db import db
import re
from sqlalchemy.orm import validates
import datetime, json


class CustomerModel(db.Model):
    """Customer model."""
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    city = db.Column(db.String(50))
    address = db.Column(db.String(200))
    birth_date = db.Column(db.String(10))
    sales = db.relationship('SaleModel', lazy='dynamic')

    def __init__(self, first_name, last_name, phone, email, city, address, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.city = city
        self.address = address
        self.birth_date = birth_date

    def json(self):
        """
        Converts this customer to JSON.

        :return: this customer.
        :rtype: JSON.
        """
        return {'first_name': self.first_name,
                'last_name': self.last_name, 'phone': self.phone, 'birth_date': self.birth_date, 'city': self.city,
                'address': self.address, 'email': self.email}

    @classmethod
    def find_by_name(cls, first_name, last_name):
        """
        Selects an customer from the DB and returns it.

        :param name: the name of the customer.
        :type name: str
        :return: an customer.
        :rtype: CustomerModel.
        """
        return (cls.query.filter_by(first_name=first_name, last_name=last_name)).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        Selects an customer from the DB and returns it.

        :param name: the name of the customer.
        :type name: str
        :return: an customer.
        :rtype: CustomerModel.
        """
        return (cls.query.filter_by(id=_id)).first()

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')
        if not re.match('[^@]+@[^@]+\\.[^@]+', email):
            raise AssertionError('Provided email is not an email address')
        return email

    @validates('birth_date')
    def validate_date(self, key, birth_date):
        if not birth_date:
            raise AssertionError('No birth_date provided')
        try:
            datetime.datetime.strptime(birth_date, '%d-%m-%Y')
        except ValueError:
            raise AssertionError('Incorrect data format, should be DD-MM-YYYY')

        return birth_date

    def save_to_db(self):
        """
        Inserts this customer in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this customer from the DB.
        """
        db.session.delete(self)
        db.session.commit()