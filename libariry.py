genre_id = ("mindset","finance","habit","motivation")
author_id = ["james clear","napoleon hill","morgan hauleg"]
books = {
    "atomic habit":{"author":author_id[0],"price":250,"pages":300,"genra":genre_id[2]},
    "think and grow rich":{"author":author_id[1],"price":300,"pages":250,"genra":genre_id[0]},
    "psychology of money":{"author":author_id[2],"price":200,"pages":200,"genra":genre_id[0]},

    }
search_by_name = input("enter the name of book: ")
search_by_genre = input("enter the genra of book: ")
search_by_author = input("enter the author name of book: ")
sort_by_price_greater = int(input("book which is greater than: "))
sort_by_price_lesser = int(input("book which is lesser than: "))
for book,detail in books.items():
    if search_by_name.lower() in book or search_by_genre.lower() in detail["genra"] or search_by_author.lower() in detail["author"]: 
        print(book)
    if sort_by_price_greater < detail["price"]:
        print("book")
    if sort_by_price_lesser > detail["price"]:
        print("book")
   
