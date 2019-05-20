
from db import db
from sqlalchemy.orm import validates
import datetime


class SaleModel(db.Model):
    """sale model."""
    __tablename__ = 'sales'
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
        Converts this sale and all its items to JSON.

        :return: this sale and all its items.
        :rtype: JSON.
        """
        return {'id': self.id,
                'total price': self.total_price,
                'payment_type': self.payment_type,
                'status': self.status,
                'cust_id': self.cust_id,
                'customer': self.customer.json()}

    @classmethod
    def find_by_id(cls, _id):
        """
        Selects a sale from the DB and returns it.

        :param name: the name of the sale.
        :type name: str
        :return: a sale.
        :rtype: saleModel.
        """
        return (cls.query.filter_by(id=_id)).first()

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
        Inserts this sale in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this sale from the DB.
        """
        db.session.delete(self)
        db.session.commit()