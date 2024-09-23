from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func

# Create the Base class, subclassed by all models
Base = declarative_base()

# Create a session to interact with the database
DATABASE_URL = 'sqlite:///bookstore.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


# Author model
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"<Author(name={self.name})>"


# Book model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    quantity = Column(Integer, default=1)

    author = relationship('Author', back_populates='books')
    sales = relationship('Sale', back_populates='book')

    def __repr__(self):
        return f"<Book(title={self.title}, price={self.price})>"


# Sale model
class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    date = Column(DateTime, default=func.now())

    book = relationship('Book', back_populates='sales')

    def __repr__(self):
        return f"<Sale(book_id={self.book_id}, quantity={self.quantity})>"
