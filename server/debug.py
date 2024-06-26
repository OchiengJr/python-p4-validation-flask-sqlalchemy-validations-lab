#!/usr/bin/env python3

from app import app
from models import db, Author, Post

if __name__ == '__main__':
    with app.app_context():
        # Initialize the database tables if they don't exist
        db.create_all()

        # Example: Create a new author
        new_author = Author(name='John Doe')
        db.session.add(new_author)
        db.session.commit()
        print(f'Added new author: {new_author}')

        # Example: Query all authors and print their names
        authors = Author.query.all()
        print('All Authors:')
        for author in authors:
            print(f'- {author.name}')

        # Enter the debugger for interactive debugging
        import ipdb; ipdb.set_trace()
