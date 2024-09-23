from database import Author, Book, session


class BookService:

    @staticmethod
    def add_book(title: str, author_name: str, price: float, stock: int):
        """Adds a new book to the store."""
        # Check if the author exists
        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            raise ValueError(
                f"Author '{author_name}' does not exist! Add the author first."
            )

        # Check if the book already exists
        existing_book = session.query(Book).filter_by(
            title=title, author_id=author.id).first()
        if existing_book:
            raise ValueError(
                f"Book '{title}' by {author_name} already exists!")

        # Create a new book
        new_book = Book(title=title,
                        author_id=author.id,
                        price=price,
                        stock=stock)
        session.add(new_book)
        session.commit()
        return new_book

    @staticmethod
    def get_all_books():
        """Lists all books in the store."""
        return session.query(Book).all()

    @staticmethod
    def get_book_by_title_and_author_name(title: str, author_name: int):
        """Fetches a book by its title and author id."""
        author = session.query(Author).filter_by(name=author_name).first()
        author_id = author.id
        return session.query(Book).filter_by(title=title,
                                             author_id=author_id).first()

    @staticmethod
    def get_book_by_id(id: int):
        """Fetchesa book by its id"""
        return session.query(Book).get(id)

    @staticmethod
    def update_book(id: int, title: str, author_name: str, price: float,
                    quantity: int):
        """Updates a book in the store."""
        book = session.query(Book).get(id)
        if not book:
            raise ValueError(f"Book with id '{id}' does not exist!")

        # Check if the author exists
        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            raise ValueError(
                f"Author '{author_name}' does not exist! Add the author first."
            )

        # Update the book
        book.title = title
        book.author_id = author.id
        book.price = price
        book.stock = quantity
        session.commit()
        return book

    @staticmethod
    def delete_book(id: int):
        """Deletes a book from the store."""
        book = session.query(Book).get(id)
        if not book:
            raise ValueError(f"Book with id '{id}' does not exist!")
        session.delete(book)
        session.commit()
