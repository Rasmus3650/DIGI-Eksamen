from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5


class Student(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    subjects = db.relationship('Subject', backref='students', lazy='dynamic')


    def __repr__(self):
        return '<Student {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)




class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now())
    description = db.Column(db.String(100), index=True)
    subject_name = db.Column(db.String(102), index=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))



    def __repr__(self):
        return '<Subject {}>'.format(self.subject_name)
