from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from booklibrary import db, login_manager, ma
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    books = db.relationship('Book', backref='user', lazy='dynamic', primaryjoin="User.id == Book.user_id") # TODO Post ex. Book & author ex owner /// DONE  posts ex. books (or booky)

    def get_reset_token(self, expires_sec=3000):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self, author, title):
        self.author = author
        self.title = title


    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class Top(db.Model):
    __tablename__ = 'tops'
    id = db.Column(db.Integer, primary_key=True)
    title1 = db.Column(db.String(100), nullable=False)
    author1 = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Top('{self.title}', '{self.author}')"

# Book Schema
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id' 'author', 'title')

# Top Schema
class TopSchema(ma.Schema):
    class Meta:
        fields = ('id', 'author1', 'title1')

# book Init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# top Init schema
top_schema = TopSchema()
tops_schema = TopSchema(many=True)