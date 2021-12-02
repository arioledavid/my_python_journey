def print_menu():
    print("""Choose an option:
    1. print all books
    2. add a book
    3. update a book
    4. delete a book
    """)

while True:
    print_menu()
    response = int(input())
    if response == 1:
        print("Printing all books")
    elif response == 2:
        print("adding a book")
    elif response == 3:
        print("Updating a book")
    elif response == 4:
        print("Deleting a book")
    else:
        print("Thanks for the using the app")
