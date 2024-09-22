"""
Script to seed the database with fake data.

The script creates a session to interact with the database, then creates 5
authors, 10 books, and 5 sales, and adds them to the database. 

The script then commits the changes to the database and closes the session.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Author, Book, Sale
import random


def create_session():
    """ Create a session to interact with the database """
    DATABASE_URL = 'sqlite:///bookstore.db'
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def seed_data():
    """Seed the database with random data"""
    print("Seeding data...")

    session = create_session()
    fake = Faker()

    # Reset the database
    session.query(Author).delete()
    session.query(Book).delete()
    session.query(Sale).delete()

    # Create 5 authors with fake data
    authors = []
    for _ in range(5):
        author = Author(name=fake.name())
        authors.append(author)
        session.add(author)

    # Pesrsist the current session to database
    session.commit()

    # Create 10 books
    books = []
    for _ in range(10):
        book_title = fake.sentence(nb_words=6)
        book_price = book_price = round(
            fake.pydecimal(left_digits=2, right_digits=2, positive=True) + 5,
            2)
        author_id = random.choice(authors).id
        book_quantity = fake.random_number(2)
        book = Book(title=book_title,
                    price=book_price,
                    author_id=author_id,
                    quantity=book_quantity)
        books.append(book)
        session.add(book)
    # Persist to database
    session.commit()

    # Create 5 sales each unique
    sales = []
    for _ in range(5):
        book_id = random.choice(books).id

        sale = Sale(book_id=book_id)
        sales.append(sale)

    # Pesrsist the current session to database
    session.add_all(sales)
    session.commit()

    print("Done seeding data.")


if __name__ == "__main__":
    seed_data()
