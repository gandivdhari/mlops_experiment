def add_book(books, book):
    books.append(book)

def update_book(books, index, updated_book):
    if 0 <= index < len(books):
        books[index] = updated_book

def delete_book(books, index):
    if 0 <= index < len(books):
        books.pop(index)

def get_books(books):
    return books

def validate_book_data(author, name, published_year, synopsis):
    if not author or not name or not published_year or not synopsis:
        return False
    if not isinstance(published_year, int) or published_year < 0:
        return False
    return True