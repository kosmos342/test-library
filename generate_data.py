#!/usr/bin/env python
import json
import random
import loremipsum
import names


AUTHOR_COUNT = 50
BOOK_COUNT = 200
MAX_WORDS_IN_TITLE = 6
MAX_AUTHORS_PER_BOOK = 4


def generate_book_title():
    words = loremipsum.generate_sentence()[2][:-1].split()
    title = ' '.join(words[:random.randrange(1, MAX_WORDS_IN_TITLE+1)])
    if title[-1] == ',':
        title = title[:-1] + '.'
    elif title[-1] != '.':
        title += '.'
    return title


def get_random_author_id():
    return random.randrange(1, AUTHOR_COUNT+1)


def get_authors():
    is_multiply_authors = random.choice([True, False])
    if is_multiply_authors:
        authors_count = random.randrange(2, MAX_AUTHORS_PER_BOOK+1)
        return list(set([
            get_random_author_id() for i in range(authors_count)
        ]))  # count of authors can be less then authors_count
    else:
        return [get_random_author_id()]


def main():
    authors = []
    author_set = set()
    i = 1
    while i <= AUTHOR_COUNT:
        author_name = names.get_full_name()
        if author_name not in author_set:
            authors.append({
                'id': i,
                'name': author_name
            })
            author_set.add(author_name)
            i += 1

    books = []
    book_set = set()
    i = 1
    while i <= BOOK_COUNT:
        book_title = generate_book_title()
        if book_title not in book_set:
            books.append({
                'id': i,
                'title': book_title,
                'authors': get_authors(),
            })
            book_set.add(book_title)
            i += 1

    data = {'authors': authors, 'books': books}
    print json.dumps(data, indent=1)


if __name__ == "__main__":
    main()
