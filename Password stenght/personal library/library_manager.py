import json
import os

LIBRARY_FILE = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Display menu
def display_menu():
    print("\n📚 Welcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == "yes"

    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    })
    print("✅ Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()

    query = input("Enter search query: ").strip().lower()
    matches = []

    if choice == "1":
        matches = [book for book in library if query in book["title"].lower()]
    elif choice == "2":
        matches = [book for book in library if query in book["author"].lower()]

    if matches:
        print("\n🔍 Matching Books:")
        for i, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("📭 Your library is empty.")
        return

    print("\n📖 Your Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display statistics
def display_stats(library):
    total = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage = (read_books / total * 100) if total > 0 else 0
    print(f"\n📊 Total books: {total}")
    print(f"📚 Percentage read: {percentage:.1f}%")

# Main program
def main():
    library = load_library()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved to file. Goodbye! 👋")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
