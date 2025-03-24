def collect_data():
    bookstore = {}

    while True:
        genre = input("Enter the book genere or type 'done' to finish: ").strip()

        if genre.lower() == 'done':
            break
    
        if genre not in bookstore:
            bookstore[genre] = {}

        while True:
            title = input(f"Enter a book title for the genre '{genre}' or type 'done' to finish: ")

            if title.lower() == 'done':
                break
            
            price = float(input(f"Enter the price of {title}: "))
            bookstore[genre][title] = price
        
    print (f"\n {bookstore}\n")
    return bookstore
    
def display_bookstore(bookstore):
    print ("\nBookstore Inventory:\n")
    for genre, books in bookstore.items():
        print (f"Genre: {genre}")
        
        for book, price in books.items():
            print (f" - {book}: ${price:.2f}")

# Collect book data from user
bookstore_invenrtory = collect_data()

# Display collected book data
display_bookstore(bookstore_invenrtory)