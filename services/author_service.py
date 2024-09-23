from database import Author, session


class AuthorService:

    @staticmethod
    def add_author(name: str):
        """Adds a new author to the database."""
        # Check if the author already exists
        existing_author = session.query(Author).filter_by(name=name).first()
        if existing_author:
            raise ValueError(f"Author '{name}' already exists!")

        # Create a new author instance
        new_author = Author(name=name)
        session.add(new_author)
        session.commit()
        return new_author

    @staticmethod
    def get_all_authors():
        """Retrieves all authors from the database."""
        return session.query(Author).all()

    @classmethod
    def get_author_by_id(id_: int):
        """Fetches an author by their id."""
        return session.query(Author).get(id_)

    @staticmethod
    def get_author_by_name(name: str):
        """Fetches an author by their name."""
        return session.query(Author).filter_by(name=name).first()

    @staticmethod
    def delete_author(name: str):
        """Deletes an author by name."""
        author = session.query(Author).filter_by(name=name).first()
        if author:
            session.delete(author)
            session.commit()
        else:
            raise ValueError(f"Author '{name}' not found!")

    @staticmethod
    def update_author(name: str, new_name: str):
        """Updates an author's name."""
        author = session.query(Author).filter_by(name=name).first()
        if author:
            author.name = new_name
            session.commit()
        else:
            raise ValueError(f"Author '{name}' not found!")
