import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading library file. Starting with an empty library.")
    return []

def save_library(library):
    try:
        with open(data_file, 'w') as file:
            json.dump(library, file, indent=4)
    except Exception as e:
        print(f"Error saving library: {e}")

def add_book(library):
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of publication: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').strip().lower() == 'yes'

    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'read': read
    }

    library.append(new_book)
    save_library(library)
    print(f"\n✅ Book '{title}' added successfully.\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    initial_length = len(library)
    updated_library = [book for book in library if book['title'].lower() != title]

    if len(updated_library) < initial_length:
        save_library(updated_library)
        print(f"\n✅ Book '{title}' removed successfully.\n")
    else:
        print(f"\n❌ Book '{title}' not found in the library.\n")

    return updated_library

def search_library(library):
    search_by = input("Search by 'title' or 'author': ").strip().lower()
    if search_by not in ['title', 'author']:
        print("❌ Invalid search option. Please choose 'title' or 'author'.")
        return

    search_term = input(f"Enter the {search_by}: ").strip().lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        print("\n📚 Search Results:")
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f" - {book['title']} by {book['author']} ({book['year']}) | {book['genre']} | {status}")
    else:
        print(f"\n❌ No books found matching '{search_term}' in the {search_by} field.\n")

def display_all_books(library):
    if library:
        print("\n📘 All Books in the Library:")
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f" - {book['title']} by {book['author']} ({book['year']}) | {book['genre']} | {status}")
    else:
        print("\n❗ The library is empty.\n")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(book['read'] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print(f"\n📊 Library Statistics:")
    print(f" - Total books: {total_books}")
    print(f" - Books read: {read_books}")
    print(f" - Percentage read: {percentage_read:.2f}%\n")

def main():
    library = load_library()

    while True:
        print("\n📚 Welcome to the Library Manager")
        print("Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search the library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            library = remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("👋 Goodbye! Have a great day.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
