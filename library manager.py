class library:
    def __init__(self, booklist, name):
        self.name = name
        self.booklist = booklist
        self.dictionary = {booklist[i]: "available" for i in range(0, len(booklist))}

    def Avalablebook(self):
        print("\n")
        for key in self.dictionary:
            if self.dictionary[key] == "available":
               print(key)
        print("\n")
    
    def Lendbook(self):
        borrowerName = input("\nEnter the borrowers name: ")
        bookName = input("Enter the book name: ")
        self.dictionary[bookName] = borrowerName
        print(f"\nMentioned\n{bookName} is with {borrowerName}\n")

    def Addbook(self):
        bookName = input("\nEnter book name: ")
        self.dictionary.update({bookName : "available"})
        print(f"\n{bookName} added\n")


    def Returnbook(self):
        giver = input("\nEnter the givers name: ")
        bookName = input("Enter the book name: ")
        self.dictionary[bookName] = "available"
        print(f"\nMentioned\n{bookName} has been returned by {giver}\n")

name = input("Enter the library name: ")
books = input("Enter the names of the books seperatd by a tab: " )
booklist = books.split("\t")
library = library(booklist, name)
print("Library Created")
while True:
    print("Enter 1 for Lend book\n2 for Recive book\n3 for available book(s)\n4 to add book")
    choice = input("Enter here: ")
    if choice == "1":
        library.Lendbook()

    elif choice == "2":
        library.Returnbook()

    elif choice == "3":
        library.Avalablebook()

    elif choice == "4":
        library.Addbook()
    else:
        print("Wrong Input\nTry again\n")
