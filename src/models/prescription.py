# uncompyle6 version 3.3.2
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\prescriptions\Delphine\PycharmProjects\MyProj\src\models\prescription.py
# Compiled at: 2019-05-14 23:54:35
# Size of source mod 2**32: 2299 bytes
from db import db
from sqlalchemy_utils import ChoiceType
from src.models import constants

class PrescriptionModel(db.Model):
    """prescriptionmodel."""
    __tablename__ = 'prescriptions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    sphere_OD = db.Column(db.Float(precision=2))
    sphere_OS = db.Column(db.Float(precision=2))
    cylinder_OD = db.Column(db.Float(precision=2))
    cylinder_OS = db.Column(db.Float(precision=2))
    axis_OD = db.Column(db.Float(precision=2))
    axis_OS = db.Column(db.Float(precision=2))
    add_OD = db.Column(db.Float(precision=2))
    add_OS = db.Column(db.Float(precision=2))
    pd = db.Column(db.Float(precision=2))
    type_name = constants.PrescriptionType
    nearsightedness = db.Column(db.Float(precision=2))
    farsightedness = db.Column(db.Float(precision=2))
    document_id = db.Column(db.String(20))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('CustomerModel')


    def __init__(self, date, sphere_OD,sphere_OS,cylinder_OD,cylinder_OS,axis_OD,axis_OS,pd,type_name,
                 nearsightedness,farsightedness,document_id,customer_id):
        self.date = date
        self.sphere_OD = sphere_OD
        self.sphere_OS = sphere_OS
        self.cylinder_OD = cylinder_OD
        self.cylinder_OS = cylinder_OS
        self.axis_OD = axis_OD
        self.axis_OS = axis_OS
        self.pd = pd
        self.type_name = type_name
        self.nearsightedness = nearsightedness
        self.farsightedness = farsightedness
        self.document_id = document_id
        self.customer_id = customer_id

    def json(self):
        """
        Converts this customer to JSON.

        :return: this customer.
        :rtype: JSON.
        """
        return {'date': self.date,'date': self.date,
                'sphere_OD': self.sphere_OD,'sphere_OS': self.sphere_OS,
                'cylinder_OD': self.cylinder_OD,'cylinder_OS': self.cylinder_OS,
                'axis_OD': self.axis_OD,'axis_OS': self.axis_OS,
                'pd': self.pd,'type_name': self.type_name,
                'nearsightedness': self.nearsightedness,'farsightedness': self.farsightedness,
                'document_id': self.document_id, 'customer_id': self.customer_id}


    @classmethod
    def find_by_id(cls, _id):
        """
        Selects a prescriptionfrom the DB and returns it.

        :param _id: the id of the prescription.
        :type _id: int
        :return: a prescription.
        :rtype: prescriptionModel.
        """
        return cls.query.filter_by(id=_id).first()



    @classmethod
    def find_all(cls):
        return cls.query().all()


    def save_to_db(self):
        """
        Inserts this prescriptionin the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this prescriptionfrom the DB.
        """
        db.session.delete(self)
        db.session.commit()
