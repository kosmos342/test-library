from flask import flash, render_template, redirect, url_for, request
from sqlalchemy import or_
from app import app, db
from .forms import AuthorForm, BookForm
from models import Book, Author


@app.route('/', defaults={'page': 1})
@app.route('/page/<int:page>/')
def book_list(page):
    paginator = Book.query.paginate(page)
    return render_template('library/book_list.html',
                           book_list=paginator.items,
                           paginator=paginator)


@app.route('/books/add/', methods=['GET', 'POST'])
@app.route('/books/<int:id>/', methods=['GET', 'POST'])
def edit_book(id=None):
    if id:
        book = Book.query.get_or_404(id)
    else:
        book = Book('')
    form = BookForm(obj=book)
    if form.validate_on_submit():
        form.populate_obj(book)
        if not id:
            db.session.add(book)
        db.session.commit()
        flash('Book "{}" was added'.format(book.title))
        return redirect(url_for('book_list'))
    return render_template('library/book_edit.html',
                           form=form, book=book)


@app.route('/authors/', defaults={'page': 1})
@app.route('/authors/page/<int:page>/')
def author_list(page):
    paginator = Author.query.paginate(page)
    return render_template('library/author_list.html',
                           author_list=paginator.items,
                           paginator=paginator)


@app.route('/authors/add/', methods=['GET', 'POST'])
@app.route('/authors/<int:id>/', methods=['GET', 'POST'])
def edit_author(id=None):
    if id:
        author = Author.query.get_or_404(id)
    else:
        author = Author('')
    form = AuthorForm(obj=author)
    if form.validate_on_submit():
        form.populate_obj(author)
        if not id:
            db.session.add(author)
        db.session.commit()
        if id:
            flash('Author "{}" was saved'.format(author.name))
        else:
            flash('Author "{}" was added'.format(author.name))
        return redirect(url_for('author_list'))
    return render_template('library/author_edit.html',
                           form=form, author=author)


def _search_query(query, q):
    return query.outerjoin(Book.authors).\
        filter(or_(Book.title.contains(q),
                   Author.name.contains(q))).\
        distinct()

@app.route('/search/', defaults={'page': 1})
@app.route('/search/page/<int:page>/')
def search(page):
    book_q = Book.query
    q = request.values.get('q', '')
    if q:
        book_q = _search_query(book_q, q)
    book_q = book_q
    paginator = book_q.paginate(page)
    return render_template('library/search.html',
                           q=q,
                           book_list=paginator.items,
                           paginator=paginator)
