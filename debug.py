from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Author, Book, Sale

if __name__ == '__main__':
    engine = create_engine('sqlite:///bookstore.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch an author, book and sale from the database
    author = session.query(Author).first()
    book = session.query(Book).first()
    sale = session.query(Sale).first()

    import ipdb
    ipdb.set_trace()
