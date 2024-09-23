from services import AuthorService, BookService, SaleService


def exit_program():
    """Exits the program, printing a goodbye message."""
    print("Goodbye!")
    exit()


# Author
def add_author():
    """
    Adds a new author to the store.

    Prompts the user for an author name, and attempts to add it to the store.
    If the addition is successful, prints a success message with the new
    author's details. If the addition fails, prints an error message.
    """
    author_name = input("Enter author name: ")
    try:
        new_author = AuthorService.add_author(author_name)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: {new_author}")


def get_all_authors():
    """
    Prints all authors in the store.

    Retrieves all authors from the store and prints them to the console.
    """
    authors = AuthorService.get_all_authors()
    for author in authors:
        print(author)


def get_author_by_id():
    """
    Retrieves an author by their id.

    Prompts the user for an author id, and attempts to retrieve it from the
    store. If the retrieval is successful, prints the author's details. If
    the retrieval fails, prints an error message.
    """
    author_id = input("Enter author id: ")
    if not author_id.isdigit():
        print("Error: Invalid author id!")
        return

    author_id = int(author_id)

    author = AuthorService.get_author_by_id(author_id)
    if author:
        print(author)
    else:
        print(f"Error: Author with id '{author_id}' not found!")


def get_author_by_name():
    """
    Retrieves an author by their name.

    Prompts the user for an author name, and attempts to retrieve it from the
    store. If the retrieval is successful, prints the author's details. If
    the retrieval fails, prints an error message.
    """
    author_name = input("Enter author name: ")
    author = AuthorService.get_author_by_name(author_name)
    if author:
        print(author)
    else:
        print(f"Error: Author '{author_name}' not found!")


def update_author():
    """
    Updates an author's name.

    Prompts the user for the author's old name and new name, and attempts to
    update the author in the store. If the update is successful, prints a
    success message. If the update fails, prints an error message.
    """
    author_name = input("Enter author name: ")
    new_name = input("Enter new name: ")
    try:
        AuthorService.update_author(author_name, new_name)
        print(f"Success: Author '{author_name}' updated!")
    except Exception as e:
        print(f"Error: {e}")


def delete_author():
    """
    Deletes an author from the store.

    Prompts the user for the author name, and attempts to delete it from the
    store. If the deletion is successful, prints a success message. If
    the deletion fails, prints an error message.
    """
    author_name = input("Enter author name: ")
    try:
        AuthorService.delete_author(author_name)
        print(f"Success: Author '{author_name}' deleted!")
    except Exception as e:
        print(f"Error: {e}")


# Book
def add_book():
    """
    Adds a new book to the store.

    Prompts the user for the book title, author name, price and quantity, and
    attempts to add the book to the store. If the addition is successful,
    prints a success message. If the addition fails, prints an error message.
    """
    book_title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    try:
        new_book = BookService.add_book(book_title, author_name, price,
                                        quantity)
        print(f"Success: {new_book} added!")
    except Exception as e:
        print(f"Error: {e}")


def get_all_books():
    """
    Prints all books in the store.

    Retrieves all books from the store and prints them to the console.
    """
    books = BookService.get_all_books()
    for book in books:
        print(book)


def get_book_by_id():
    """
    Retrieves a book by its id.

    Prompts the user for a book id, and attempts to retrieve it from the
    store. If the retrieval is successful, prints the book's details. If
    the retrieval fails, prints an error message.
    """
    book_id = input("Enter book id: ")
    if not book_id.isdigit():
        print("Error: Invalid book id!")
        return

    book_id = int(book_id)

    book = BookService.get_book_by_id(book_id)
    if book:
        print(book)
    else:
        print(f"Error: Book with id '{book_id}' not found!")


def get_book_by_title_and_author_name():
    """
    Retrieves a book by its title and author name.

    Prompts the user for a book title and author name, and attempts to
    retrieve the book from the store. If the retrieval is successful,
    prints the book's details. If the retrieval fails, prints an error
    message.
    """
    book_title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    book = BookService.get_book_by_title_and_author_name(
        book_title, author_name)
    if book:
        print(book)
    else:
        print(f"Error: Book '{book_title}' by {author_name} not found!")


def update_book():
    """
    Updates a book in the store.

    Prompts the user for the book's id, new title, new author name, new price,
    and new quantity, and attempts to update the book in the store. If the
    update is successful, prints a success message. If the update fails,
    prints an error message.
    """
    book_id = input("Enter book id: ")
    if not book_id.isdigit():
        print("Error: Invalid book id!")
        return
    quantity = input("Enter new quantity: ")
    if not quantity.isdigit():
        print("Error: Invalid quantity!")
        return
    price = input("Enter new price: ")
    if not price.isdigit():
        print("Error: Invalid price!")
        return

    book_id = int(book_id)
    quantity = int(quantity)
    price = float(price)
    title = input("Enter new title: ")
    author_name = input("Enter new author name: ")

    try:
        new_book = BookService.update_book(book_id, title, author_name, price,
                                           quantity)
        print(f"Success:  {new_book} updated!")
    except Exception as e:
        print(f"Error: {e}")


def delete_book():
    """
    Deletes a book from the store.

    Prompts the user for the book id, and attempts to delete the book from
    the store. If the deletion is successful, prints a success message. If
    the deletion fails, prints an error message.
    """
    book_id = input("Enter book id: ")
    if not book_id.isdigit():
        print("Error: Invalid book id")

    book_id = int(book_id)

    try:
        BookService.delete_book(book_id)
        print(f"Success: Book with id '{book_id}' deleted!")
    except Exception as e:
        print(f"Error: {e}")


# Sales
def sell_book():
    """
    Processes a book sale.

    Prompts the user for the book title, author name and quantity, and
    attempts to add a new sale to the store. If the addition is successful,
    prints a success message with the new sale's details. If the addition
    fails, prints an error message.
    """
    book_title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    quantity = input("Enter quantity: ")
    if not quantity.isdigit():
        print('Error: Invalid quantity!')
        return

    try:
        new_sale = SaleService.sell_book(book_title, author_name, quantity)
        print(f"Success: {new_sale} added!")
    except Exception as e:
        print(f"Error: {e}")


def get_all_sales():
    """
    Prints all sales in the store.

    Retrieves all sales from the store and prints them to the console.
    """
    sales = SaleService.get_all_sales()
    for sale in sales:
        print(sale)


def get_sale_by_id():
    """
    Retrieves a sale by its id.

    Prompts the user for a sale id, and attempts to retrieve it from the
    store. If the retrieval is successful, prints the sale's details. If
    the retrieval fails, prints an error message.
    """
    id_ = input("Enter sale id: ")
    if not id_.isdigit():
        print("Error: Invalid ID!")
        return
    id_ = int(id)

    sale = SaleService.get_sale_by_id(id_)

    if sale:
        print(sale)
    else:
        print(f"Error: Sale with id '{id_}' not found!")


def update_sale():
    """
    Updates a sale in the store.

    Prompts the user for the sale id, new quantity and new book id.
    If the update is successful, prints a success message. If the update
    fails, prints an error message.
    """
    id_ = input("Enter sale id: ")
    if not id_.isdigit():
        print("Error: Invalid ID!")
        return
    id_ = int(id_)
    quantity = input("Enter new quantity: ")
    book_id = input("Enter new book id: ")

    try:
        new_sale = SaleService.update_sale(id_, quantity, book_id)
        print(f"Success: {new_sale} updated!")
    except Exception as e:
        print(f"Error: {e}")


def delete_sale():
    """
    Deletes a sale from the store.

    Prompts the user for the sale id.
    If the deletion is successful, prints a success message. If the deletion
    fails, prints an error message.
    """
    id_ = input("Enter sale id: ")
    if not id_.isdigit():
        print("Errror: Invalid ID!")
        return
    id_ = int(id_)

    try:
        SaleService.delete_sale(id_)
        print(f"Success: Sale with id '{id_}' deleted!")
    except Exception as e:
        print(f"Error: {e}")
