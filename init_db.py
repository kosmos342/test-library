#!/usr/bin/env python
import json
import sys
from app import db
from app.library.models import Author, Book


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'initial_data.json'
    db.create_all()
    data = json.loads(open(filename).read())

    authors_ids = {}

    for author in data['authors']:
        a = Author(author['name'])
        a.id = author['id']
        authors_ids[a.id] = a
        db.session.add(a)

    for book in data['books']:
        b = Book(book['title'])
        b.id = book['id']
        b.authors = [authors_ids[a] for a in book['authors']]
        db.session.add(b)

    db.session.commit()


if __name__ == "__main__":
    main()
