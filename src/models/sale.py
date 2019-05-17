# uncompyle6 version 3.3.2
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Users\Delphine\PycharmProjects\MyProj\src\models\sale.py
# Compiled at: 2019-05-14 22:37:50
# Size of source mod 2**32: 2274 bytes
"""
| Created: 2017-08-13
| Updated: 2017-08-13
"""
from db import db
from sqlalchemy.orm import validates
import datetime


class SaleModel(db.Model):
    """Sale model."""
    __tablename__ = 'sales_order'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    total_price = db.Column(db.Float(precision=2))
    payment_type = db.Column(db.String(50))
    status = db.Column(db.String(50))
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('CustomerModel')

    def __init__(self, date, total_price, payment_type, status, cust_id):
        self.date = date
        self.total_price = total_price
        self.payment_type = payment_type
        self.status = status
        self.cust_id = cust_id

    def json(self):
        """
        Converts this store and all its items to JSON.

        :return: this store and all its items.
        :rtype: JSON.
        """
        return {'id': self.id,
                'total price': self.total_price,
                'payment_type': self.payment_type,
                'status': self.status,
                'cust_id': self.cust_id,
                'customer': self.customer.json()}

    @classmethod
    def find_by_id(cls, id):
        """
        Selects a store from the DB and returns it.

        :param name: the name of the store.
        :type name: str
        :return: a store.
        :rtype: StoreModel.
        """
        return (cls.query.filter_by(id=id)).first()

    @validates('date')
    def validate_date(self, key, date):
        if not date:
            raise AssertionError('No date provided')
        if date:
            try:
                datetime.datetime.strptime(date, '%d-%m-%Y')
            except ValueError:
                raise AssertionError('Incorrect data format, should be DD-MM-YYYY')

            return date

    def save_to_db(self):
        """
        Inserts this store in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this store from the DB.
        """
        db.session.delete(self)
        db.session.commit()