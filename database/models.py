from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Date
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

# Create the Base class, subclassed by all models
Base = declarative_base()

# Association table for many-to-many relationshi between Sale and Book
books_sales = Table('books_sales',
                    Base.metadata,
                    Column('sale_id',
                           Integer,
                           ForeignKey('sales.id'),
                           primary_key=True),
                    Column('book_id',
                           Integer,
                           ForeignKey('books.id'),
                           primary_key=True),
                    Column('purchase_date', Date, default=func.now()),
                    extend_existing=True)


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
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')
    sales = relationship('Sale', secondary=books_sales, back_populates='books')

    def __repr__(self):
        return f"<Book(title={self.title}, price={self.price})>"


# Sale model
class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer, nullable=False)

    books = relationship('Book', secondary=books_sales, back_populates='sales')

    def __repr__(self):
        return f"<Sale(book_id={self.book_id}, quantity={self})>"
