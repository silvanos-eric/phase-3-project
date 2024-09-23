from helpers import (exit_program, get_all_authors, get_author_by_id,
                     get_author_by_name, add_author, update_author,
                     delete_author, get_all_books, get_book_by_id,
                     get_book_by_title_and_author_name, add_book, update_book,
                     delete_book, get_all_sales, get_sale_by_id, update_sale,
                     delete_sale)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_authors()
        elif choice == "2":
            get_author_by_id()
        elif choice == "3":
            get_author_by_name()
        elif choice == "4":
            add_author()
        elif choice == "5":
            update_author()
        elif choice == "6":
            delete_author()
        elif choice == "7":
            get_all_books()
        elif choice == "8":
            get_book_by_id()
        elif choice == "9":
            get_book_by_title_and_author_name()
        elif choice == "10":
            add_book()
        elif choice == "11":
            update_book()
        elif choice == "12":
            delete_book()
        elif choice == "13":
            get_all_sales()
        elif choice == "14":
            get_sale_by_id()
        elif choice == "15":
            update_sale()
        elif choice == "16":
            delete_sale()
        else:
            print("Invalid choice. Please try again.")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all authors")
    print("2. Find an author by id")
    print("3. Find an author by name")
    print("4. Create an author")
    print("5. Update an author")
    print("6. Delete an author")
    print("7. List all books")
    print("8. Find a book by id")
    print("9. Find a book by title and author name")
    print("10. Create a book")
    print("11. Update a book")
    print("12. Delete a book")
    print("13. List all sales")
    print("14. Find a sale by id")
    print("15. Update a sale")
    print("16. Delete a sale")
