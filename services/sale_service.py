from database import Sale, session, Book
from . import BookService, AuthorService


class SalesService:

    @staticmethod
    def sell_book(title: str, author_name: str, quantity: int):
        """Processes a book sale."""
        # Fetch the book
        author = AuthorService.get_author_by_name(author_name)
        author_id = author.id

        book = BookService.get_book_by_title_and_author_id(title, author_id)
        if not book:
            raise ValueError(f"Book '{title}' by {author_name} not found!")

        # Check if stock is sufficient
        if book.stock < quantity:
            raise ValueError(
                f"Not enough stock for '{title}'. Available: {book.stock}")

        # Record the sale
        sale = Sale(book_id=book.id, quantity=quantity)
        session.add(sale)

        # Update the stock of the book
        book.stock -= quantity
        session.commit()

        return sale

    @staticmethod
    def get_all_sales():
        """Lists all sales transactions."""
        return session.query(Sale).all()

    @staticmethod
    def get_sale_by_id(id_: int):
        return session.query(Sale).get(id_)

    @staticmethod
    def update_sale(id_: int, quantity: int, book_id: int):
        sale = session.query(Sale).get(id_)
        if not sale:
            raise ValueError(f"Sale with id '{id_}' does not exist!")
        book = session.query(Book).get(book_id)
        if not book:
            raise ValueError(f"Book with id '{book_id}' does not exist!")

        sale.quantity = quantity
        sale.book_id = book_id
        session.commit()
        return sale

    @staticmethod
    def delete_sale(id_: int):
        sale = session.query(Sale).get(id_)
        if not sale:
            raise ValueError(f"Sale with id '{id_}' does not exist!")
        session.delete(sale)
        session.commit()
