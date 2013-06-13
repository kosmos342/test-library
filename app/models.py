from app import db


book_author_assc_table = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, unique=True)
    authors = db.relationship('Author', secondary=book_author_assc_table,
                              backref=db.backref('books', lazy='dynamic'))

    def __repr__(self):
        return '<Book %r>' % self.title


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)

    def __repr__(self):
        return '<Author %r>' % self.name