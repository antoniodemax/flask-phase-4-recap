from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

# Association table between User and Group
user_groups = db.Table('user_groups',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),  # Changed to 'user.id'
                       db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
                       )

class User(db.Model, SerializerMixin):
    __tablename__ = 'user'  # Ensure consistency by using 'user'

    serialize_rules = ('-posts.user', '-groups.users')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120))

    # One-to-many relationship with Post
    posts = db.relationship('Post', back_populates='user')
    
    # Many-to-many relationship with Group through user_groups association table
    groups = db.relationship('Group', secondary=user_groups, back_populates='users')

    # Email validation using @validates decorator
    @validates('email')
    def validate_email(self, key, value):
        if '@' not in value:
            raise ValueError('Email must contain @ symbol')
        return value

    # def __repr__(self):
    #     return f'<User {self.username}>'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Foreign key to User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Ensure it references 'user.id'
    
    # Relationship back to User
    user = db.relationship('User', back_populates='posts')

    # def __repr__(self):
    #     return f'<Post {self.title}>'

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    # Many-to-many relationship with User through user_groups association table
    users = db.relationship('User', secondary=user_groups, back_populates='groups')

    # def __repr__(self):
    #     return f'<Group {self.name}>'
