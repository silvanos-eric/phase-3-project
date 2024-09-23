# Bookstore Management System

## Table of Contents
- [Bookstore Management System](#bookstore-management-system)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Available Commands](#available-commands)
  - [Project Structure](#project-structure)
  - [API Reference](#api-reference)
    - [Models](#models)
    - [Services](#services)
  - [License](#license)
  - [Contributing](#contributing)
  - [Authors](#authors)

## Description
A simple command-line application to manage a bookstore's inventory and sales. This application allows users to manage authors, books, and sales using a SQLite database.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/silvanos-eric/phase-3-project.git
   cd phase-3-project
   ```

2. Install dependencies:
   ```bash
   pip install pipenv
   pipenv install
   ```

3. Initialize the database:
   ```bash
   python src/seed.py
   ```

## Usage

To start the application, run:
```bash
python src/cli.py
```

You will be presented with a menu to manage authors, books, and sales.

### Available Commands
- List all authors
- Find an author by ID or name
- Add, update, or delete authors
- List all books
- Find a book by title or author
- Add, update, or delete books
- List all sales
- Find a sale by ID
- Update or delete sales

## Project Structure
```
.
├── LICENSE.md
├── Pipfile
├── Pipfile.lock
└── src
    ├── alembic.ini
    ├── bookstore.db
    ├── cli.py
    ├── debug.py
    ├── helpers
    │   ├── cli.py
    │   └── __init__.py
    ├── migrations
    ├── models.py
    ├── seed.py
    └── services
        ├── author_service.py
        ├── book_service.py
        ├── __init__.py
        └── sale_service.py
```

## API Reference

### Models
- **Author**: Represents authors in the bookstore.
- **Book**: Represents books, including title, price, and stock.
- **Sale**: Represents sales transactions for books.

### Services
- **AuthorService**: Manages authors.
- **BookService**: Manages books.
- **SaleService**: Manages sales transactions.

## License
This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on the [GitHub repository](https://github.com/silvanos-eric/phase-3-project.git).

## Authors
- [Silvanos Eric](https://github.com/silvanos-eric)