# uncompyle6 version 3.3.2
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Users\Delphine\PycharmProjects\MyProj\src\models\customer.py
# Compiled at: 2019-05-16 19:11:03
# Size of source mod 2**32: 3068 bytes
"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
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
    sales_orders = db.relationship('Sale_OrderModel', lazy='dynamic')

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
        Converts this item to JSON.

        :return: this item.
        :rtype: JSON.
        """
        return {'first_name': self.first_name,
                'last_name': self.last_name, 'phone': self.phone, 'birth_date': self.birth_date, 'city': self.city,
                'address': self.address, 'email': self.email}

    @classmethod
    def find_by_name(cls, first_name, last_name):
        """
        Selects an customer from the DB and returns it.

        :param name: the name of the item.
        :type name: str
        :return: an item.
        :rtype: CustomerModel.
        """
        return (cls.query.filter_by(first_name=first_name, last_name=last_name)).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        Selects an item from the DB and returns it.

        :param name: the name of the item.
        :type name: str
        :return: an item.
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
        Inserts this item in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this item from the DB.
        """
        db.session.delete(self)
        db.session.commit()