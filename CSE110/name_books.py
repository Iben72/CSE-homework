with open("books.txt") as names_book:
     for line in names_book:
          book = line.strip("names_book")
          print(book)