from flask.ext.wtf import Form, Required
from wtforms.ext.sqlalchemy.orm import model_form
from app import db
from .models import Author, Book


BaseBookForm = model_form(Book, db_session=db.session, base_class=Form,
                      field_args={'authors': {'validators': [Required()]}})


class BookForm(BaseBookForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)


AuthorForm = model_form(Author, db_session=db.session, base_class=Form)
