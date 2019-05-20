# uncompyle6 version 3.3.2
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\prescriptions\Delphine\PycharmProjects\MyProj\src\models\prescription.py
# Compiled at: 2019-05-14 23:54:35
# Size of source mod 2**32: 2299 bytes
from db import db
from sqlalchemy.orm import validates
import re
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_utils import ChoiceType
import macros

class PrescriptionModel(db.Model):
    """prescriptionmodel."""
    __tablename__ = 'prescriptions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    Sphere_OD = db.Column(db.Float(precision=2))
    Sphere_OS = db.Column(db.Float(precision=2))
    Cylinder_OD = db.Column(db.Float(precision=2))
    Cylinder_OS = db.Column(db.Float(precision=2))
    Axis_OD = db.Column(db.Float(precision=2))
    Axis_OS = db.Column(db.Float(precision=2))
    Add_OD = db.Column(db.Float(precision=2))
    Add_OS = db.Column(db.Float(precision=2))
    Pd = db.Column(db.Float(precision=2))
    Type_ID = ChoiceType(macros.PRESCRIPTION_TYPE)
    Nearsightedness = db.Column(db.Float(precision=2))
    Farsightedness = db.Column(db.Float(precision=2))
    Document_ID = db.Column(db.String(20))
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('CustomerModel')


    def __init__(self, date, Sphere_OD,Sphere_OS,Cylinder_OD,Cylinder_OS,Axis_OD,Axis_OS,Pd,Type_ID,
                 Nearsightedness,Farsightedness,Document_ID,cust_id):
        self.date = date
        self.Sphere_OD = Sphere_OD
        self.Sphere_OS = Sphere_OS
        self.Cylinder_OD = Cylinder_OD
        self.Cylinder_OS = Cylinder_OS
        self.Axis_OD = Axis_OD
        self.Axis_OS = Axis_OS
        self.Pd = Pd
        self.Type_ID = Type_ID
        self.Nearsightedness = Nearsightedness
        self.Farsightedness = Farsightedness
        self.cust_id = cust_id


    @classmethod
    def find_by_id(cls, _id):
        """
        Selects a prescriptionfrom the DB and returns it.

        :param _id: the id of the prescription.
        :type _id: int
        :return: a prescription.
        :rtype: prescriptionModel.
        """
        return (cls.query.filter_by(id=_id)).first()


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

    # class PrescriptionModelForm(ModelForm):
    #     class Meta:
    #         model = PrescriptionModel