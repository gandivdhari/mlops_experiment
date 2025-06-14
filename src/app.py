import streamlit as st
from utils import add_book, update_book, delete_book, get_books, validate_book_data

st.title("📚 Book Collection App")

# Initialize books in session state
if "books" not in st.session_state:
    st.session_state.books = []

menu = st.sidebar.selectbox("Menu", ["Add Book", "View Books", "Update Book", "Delete Book"])

if menu == "Add Book":
    st.header("Add a New Book")
    author = st.text_input("Author")
    name = st.text_input("Book Name")
    published_year = st.number_input("Published Year", min_value=0, step=1, format="%d")
    synopsis = st.text_area("Synopsis")

    if st.button("Add Book"):
        if validate_book_data(author, name, int(published_year), synopsis):
            book = {
                "author": author,
                "name": name,
                "published_year": int(published_year),
                "synopsis": synopsis
            }
            add_book(st.session_state.books, book)
            st.success("Book added successfully!")
        else:
            st.error("Please fill all fields correctly.")

elif menu == "View Books":
    st.header("All Books")
    books = get_books(st.session_state.books)
    if books:
        for idx, book in enumerate(books):
            st.markdown(f"**{idx+1}. {book['name']}** by {book['author']} ({book['published_year']})")
            st.write(book['synopsis'])
            st.markdown("---")
    else:
        st.info("No books in the collection.")

elif menu == "Update Book":
    st.header("Update a Book")
    books = get_books(st.session_state.books)
    if books:
        book_options = [f"{b['name']} by {b['author']}" for b in books]
        selected = st.selectbox("Select a book to update", book_options)
        idx = book_options.index(selected)
        book = books[idx]

        author = st.text_input("Author", value=book["author"])
        name = st.text_input("Book Name", value=book["name"])
        published_year = st.number_input("Published Year", min_value=0, step=1, value=book["published_year"], format="%d")
        synopsis = st.text_area("Synopsis", value=book["synopsis"])

        if st.button("Update Book"):
            if validate_book_data(author, name, int(published_year), synopsis):
                updated_book = {
                    "author": author,
                    "name": name,
                    "published_year": int(published_year),
                    "synopsis": synopsis
                }
                update_book(st.session_state.books, idx, updated_book)
                st.success("Book updated successfully!")
            else:
                st.error("Please fill all fields correctly.")
    else:
        st.info("No books to update.")

elif menu == "Delete Book":
    st.header("Delete a Book")
    books = get_books(st.session_state.books)
    if books:
        book_options = [f"{b['name']} by {b['author']}" for b in books]
        selected = st.selectbox("Select a book to delete", book_options)
        idx = book_options.index(selected)
        if st.button("Delete Book"):
            delete_book(st.session_state.books, idx)
            st.success("Book deleted successfully!")
    else:
        st.info("No books to delete.")