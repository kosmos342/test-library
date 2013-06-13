from flask import flash, render_template, redirect, request, url_for
from app import app, db
from .forms import BookForm, AuthorForm
from .models import Book, Author


@app.route('/')
def book_list():
    book_list = Book.query.all()
    return render_template('library/book_list.html', book_list=book_list)


@app.route('/books/add/', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        # can't save m2m for now
        book = Book(form.data['title'])
        db.session.add(book)
        db.session.commit()
        flash('Book "{}" was added'.format(book.title))
        return redirect(url_for('book_list'))
    return render_template('library/book_add.html', form=form)


@app.route('/authors/')
def author_list():
    author_list = Author.query.all()
    return render_template('library/author_list.html', author_list=author_list)


@app.route('/authors/add/', methods=['GET', 'POST'])
def add_author():
    form = AuthorForm()
    if form.validate_on_submit():
        a = Author(**form.data)
        db.session.add(a)
        db.session.commit()
        flash('Author "{}" was added'.format(a.name))
        return redirect(url_for('author_list'))
    return render_template('library/author_add.html', form=form)