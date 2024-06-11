# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.



library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
new_book = ('Escaping the  Build Trap', 'Melissa Perri')


def add_book(atuple):
    if isinstance(atuple, tuple) and atuple not in library:
        library.append(atuple)
        print(f"{atuple} has been added to the library!")
        print(f"Complete library list: {library}")
    elif isinstance(atuple, tuple) and atuple in library:
        print("Will not add to library. Book is already in library")
        print(f"Complete library list: {library}")


add_book(new_book)
