from models import Author, session


class AuthorService:

    @staticmethod
    def add_author(name: str):
        """Adds a new author to the database."""
        if name is None:
            raise ValueError("Author name cannot be None!")
        if not isinstance(name, str):
            raise TypeError("Author name must be a string!")
        if len(name.strip()) == 0:
            raise ValueError("Author name cannot be empty!")

        # Check if the author already exists
        existing_author = session.query(Author).filter_by(name=name).first()
        if existing_author:
            raise ValueError(f"Author '{name}' already exists!")

        # Create a new author instance
        new_author = Author(name=name)
        session.add(new_author)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        return new_author

    @staticmethod
    def get_all_authors():
        """Retrieves all authors from the database."""
        authors = session.query(Author).all()
        if authors is None:
            raise ValueError("No authors found!")
        return authors

    @staticmethod
    def get_author_by_id(id_: int):
        """Fetches an author by their id."""
        if id_ is None:
            raise ValueError("Author id cannot be None!")
        if not isinstance(id_, int):
            raise TypeError("Author id must be an integer!")
        author = session.query(Author).get(id_)
        if author is None:
            raise ValueError(f"Author with id '{id_}' not found!")
        return author

    @staticmethod
    def get_author_by_name(author_name: str) -> Author:
        """Fetches an author by their name."""
        if not author_name:
            raise ValueError("Author name cannot be empty!")

        author = session.query(Author).filter_by(name=author_name).first()
        if author is None:
            raise ValueError(f"Author '{author_name}' not found!")
        return author

    @staticmethod
    def delete_author(name: str):
        """Deletes an author by name."""
        if not name:
            raise ValueError("Author name cannot be empty!")

        author = session.query(Author).filter_by(name=name).first()
        if author is None:
            raise ValueError(f"Author '{name}' not found!")

        session.delete(author)
        session.commit()

    @staticmethod
    def update_author(name: str, new_name: str):
        """Updates an author's name."""
        if not name or not new_name:
            raise ValueError("Author name and new name cannot be empty!")

        author = session.query(Author).filter_by(name=name).first()
        if author is None:
            raise ValueError(f"Author '{name}' not found!")

        author.name = new_name
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
