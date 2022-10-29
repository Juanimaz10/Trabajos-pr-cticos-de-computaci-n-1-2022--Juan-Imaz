import Book
import Client

book_list = []
customer_list = []
book_number = 0
client_number = 0

start = True
while start:
    print("""
    -******-
    | MENÚ |
    -******-
----------------------------------------------------
🅐 1) - Add a book
🅑 2) - Show Book (You need to know the book_number)
🅒 3) - Add a client
🅓 4) - Show client (You need to know the client_number)
🅔 5) - Exit
----------------------------------------------------""")
    option = int(input("Enter the option that you want: "))
    if option == 1:
        title = str(input("Insert the title of the book: "))
        author_name = str(input("Insert the name of the author: "))
        author_lastname = str(input("Insert the lastname of the author: "))
        author = author_name + " " + author_lastname
        price = int(input("Insert the price of the book: "))
        book = Book.Book(title, author, price)
        if book_number == 0:
            book_list.append(book)
            print("\n----------Saved book in number: 0 (remember this number to find the book)----------")
            book_number = 1
        else:
            book_list.insert(book_number, book)
            print("\n----------Saved book in the number: {}"
                  " (remember this number to find the book)----------".format(book_number))
            book_number += 1
    elif option == 2:
        book_number = int(input("Insert the number of the book that you want to know: "))
        print(book_list[book_number])
    elif option == 3:
        name_client = str(input("Insert the name of the client: "))
        lastname_client = str(input("Insert the lastname of the client: "))
        client = name_client + " " + lastname_client
        age = int(input("Insert the age of the client: "))
        address = str(input("Insert the address of the client: "))
        client = Client.Client(client, age, address)
        if client_number == 0:
            customer_list.append(client)
            print("\n----------Saved client in the number: 0 (remember this number to find it)----------")
            client_number = 1
        else:
            book_list.insert(client_number, client)
            print("\n----------Cliente guardado en el indice: {}"
                  " (recuerde este número para poder buscarlo)----------".format(client_number))
            client_number += 1
    elif option == 4:
        client_number= int(input("Insert the name of the client to find it: "))
        print(customer_list[client_number])
    elif option == 5:
        start = False