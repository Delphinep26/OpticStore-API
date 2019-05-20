# uncompyle6 version 3.3.2
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Prescriptions\Delphine\PycharmProjects\MyProj\src\models\Prescription.py
# Compiled at: 2019-05-14 23:54:35
# Size of source mod 2**32: 2299 bytes
from db import db
from sqlalchemy.orm import validates
import re
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_utils import ChoiceType

PRESCRIPTION_TYPE = [('Single_Vision','Single_Vision'),('Multifocal_Lenses','Multifocal Lenses')
                    ,('Bifocal','Bifocal'),('Progressive','Progressive'),('Computer_Glasses','Reading')]

class PrescriptionModel(db.Model):
    """prescriptionmodel."""
    __tablename__ = 'Prescriptions'
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
    Type_ID = ChoiceType(PRESCRIPTION_TYPE)
    Nearsightedness = db.Column(db.Float(precision=2))
    Farsightedness = db.Column(db.Float(precision=2))
    Document_ID = db.Column(db.String(20))
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('CustomerModel')


    def __init__(self, username, password):
        self.username = username
        self.password = password

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
        Type_ID = ChoiceType(PRESCRIPTION_TYPE)
        Nearsightedness = db.Column(db.Float(precision=2))
        Farsightedness = db.Column(db.Float(precision=2))
        Document_ID = db.Column(db.String(20))
        cust_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
        customer = db.relationship('CustomerModel')

    @classmethod
    def find_by_username(cls, username):
        """
        Selects a prescriptionfrom the DB and returns it.

        :param username: the username of the Prescription.
        :type username: str
        :return: a Prescription.
        :rtype: PrescriptionModel.
        """
        return (cls.query.filter_by(username=username)).first()

    @classmethod
    def find_by_id(cls, _id):
        """
        Selects a prescriptionfrom the DB and returns it.

        :param _id: the id of the Prescription.
        :type _id: int
        :return: a Prescription.
        :rtype: PrescriptionModel.
        """
        return (cls.query.filter_by(id=_id)).first()

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if PrescriptionModel.query.filter(PrescriptionModel.username == username).first():
            raise AssertionError('username is already in use')
        if len(username) < 5 or len(username) > 20:
            raise AssertionError('username must be between 5 and 20 characters')
        return username

    @validates('password')
    def validate_password(self, key, password):
        if not password:
            raise AssertionError('Password not provided')
        if not re.match('\\d.*[A-Z]|[A-Z].*\\d', password):
            raise AssertionError('Password must contain 1 capital letter and 1 number')
        if len(password) < 8 or len(password) > 20:
            raise AssertionError('Password must be between 8 and 20 characters')
        return password

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

    class PrescriptionForm(ModelForm):
        class Meta:
            model = PrescriptionModel