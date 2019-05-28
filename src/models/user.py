# uncompyle6 version 3.3.2
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Users\Delphine\PycharmProjects\MyProj\src\models\user.py
# Compiled at: 2019-05-14 23:54:35
# Size of source mod 2**32: 2299 bytes
from db import db
from sqlalchemy.orm import validates
import re
#from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    """User model."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'username': self.username
        }

    @classmethod
    def find_by_username(cls, username):
        """
        Selects a user from the DB and returns it.

        :param username: the username of the user.
        :type username: str
        :return: a user.
        :rtype: UserModel.
        """

        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls,_id):
        """
        Selects a user from the DB and returns it.

        :param _id: the id of the user.
        :type _id: int
        :return: a user.
        :rtype: UserModel.
        """
        print(_id)
        return cls.query.filter_by(id=_id).first()

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')
        if UserModel.query.filter(UserModel.username == username).first():
            raise AssertionError('Username is already in use')
        if len(username) < 5 or len(username) > 20:
            raise AssertionError('Username must be between 5 and 20 characters')
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
        Inserts this user in the DB.
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """
        Deletes this user from the DB.
        """
        db.session.delete(self)
        db.session.commit()