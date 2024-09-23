from services import AuthorService, BookService, SaleService


def exit_program():
    print("Goodbye!")
    exit()


# Author
def add_author():
    author_name = input("Enter author name: ")
    try:
        new_author = AuthorService.add_author(author_name)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: {new_author}")


def get_all_authors():
    authors = AuthorService.get_all_authors()
    for author in authors:
        print(author)


def get_author_by_id():
    author_id = int(input("Enter author id: "))
    author = AuthorService.get_author_by_id(author_id)
    if author:
        print(author)
    else:
        print(f"Error: Author with id '{author_id}' not found!")


def get_author_by_name():
    author_name = input("Enter author name: ")
    author = AuthorService.get_author_by_name(author_name)
    if author:
        print(author)
    else:
        print(f"Error: Author '{author_name}' not found!")


def update_author():
    author_name = input("Enter author name: ")
    new_name = input("Enter new name: ")
    try:
        AuthorService.update_author(author_name, new_name)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: Author '{author_name}' updated!")


def delete_author():
    author_name = input("Enter author name: ")
    try:
        AuthorService.delete_author(author_name)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: Author '{author_name}' deleted!")


# Book
def add_book():
    book_title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    try:
        new_book = BookService.add_book(book_title, author_name, price,
                                        quantity)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: {new_book} added!")


def get_all_books():
    books = BookService.get_all_books()
    for book in books:
        print(book)


def get_book_by_id():
    book_id = int(input("Enter book id: "))
    book = BookService.get_book_by_id(book_id)
    if book:
        print(book)
    else:
        print(f"Error: Book with id '{book_id}' not found!")


def get_book_by_title_and_author_name():
    book_title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    book = BookService.get_book_by_title_and_author_name(
        book_title, author_name)
    if book:
        print(book)
    else:
        print(f"Error: Book '{book_title}' by {author_name} not found!")


def update_book():
    book_id = int(input("Enter book id: "))
    title = input("Enter new title: ")
    author_name = input("Enter new author name: ")
    price = float(input("Enter new price: "))
    quantity = int(input("Enter new quantity: "))

    try:
        new_book = BookService.update_book(book_id, title, author_name, price,
                                           quantity)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success:  {new_book} updated!")


def delete_book():
    book_id = int(input("Enter book id: "))
    try:
        BookService.delete_book(book_id)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: Book with id '{book_id}' deleted!")


# Sales
def sell_book():
    book_title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    quantity = int(input("Enter quantity: "))
    try:
        new_sale = SaleService.sell_book(book_title, author_name, quantity)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: {new_sale} added!")


def get_all_sales():
    sales = SaleService.get_all_sales()
    for sale in sales:
        print(sale)


def get_sale_by_id():
    id_ = input("Enter sale id: ")
    sale = SaleService.get_sale_by_id(id_)

    if sale:
        print(sale)
    else:
        print(f"Error: Sale with id '{id_}' not found!")


def update_sale():
    id_ = input("Enter sale id: ")
    quantity = input("Enter new quantity: ")
    book_id = input("Enter new book id: ")
    try:
        new_sale = SaleService.update_sale(id_, quantity, book_id)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: {new_sale} updated!")


def delete_sale():
    id_ = input("Enter sale id: ")
    try:
        SaleService.delete_sale(id_)
    except Exception as e:
        print(f"Error: {e}")
    print(f"Success: Sale with id '{id_}' deleted!")
