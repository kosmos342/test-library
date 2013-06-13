from flask.ext.wtf import Form, TextField, Required, Length, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.ext.sqlalchemy.validators import Unique
from app import db
from .models import Author, Book


class BookForm(Form):
    title = TextField('title', validators=[
        Required(),
        Length(max=255),
        Unique(db.session, Book, Book.title, 'Such book already exists')
    ])
    authors = QuerySelectMultipleField('authors', validators=[Required()],
                                       query_factory=Author.query.all)


class AuthorForm(Form):
    name = TextField('name', validators = [
        Required(),
        Length(max=255),
        Unique(db.session, Author, Author.name, 'Such author already exists')
    ])