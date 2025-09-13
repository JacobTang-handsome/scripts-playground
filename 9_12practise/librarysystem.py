class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.max_books = 3

    def borrow_books(self, book):
        if book.borrow() and len(self.borrowed_books) < self.max_books:
            self.borrowed_books.append(book)
            return True
        return False

    def return_books(self, book):
        if book.return_book() and book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False

    def list_borrowed_books(self):
        return [book.title for book in self.borrowed_books]


class library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def list_available_books(self):
        return [book.title for book in self.books if not book.is_borrowed]

    def list_members(self):
        return [member.name for member in self.members]


# Example usage:
lib = library()
book1 = book("1984", "George Orwell")
book2 = book("To Kill a Mockingbird", "Harper Lee")
book3 = book("The Great Gatsby", "F. Scott Fitzgerald")
book4 = book("Moby Dick", "Herman Melville")
member1 = member("tang", 1)
member2 = member("zi", 2)
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)
lib.register_member(member1)
lib.register_member(member2)
print("Available books:", lib.list_available_books())
member1.borrow_books(book1)
member1.borrow_books(book2)
print("Member1 borrowed books:", member1.list_borrowed_books())
print("Available books after Member1 borrows:", lib.list_available_books())
member1.return_books(book1)
print("Member1 borrowed books after returning one:",
      member1.list_borrowed_books())
print("Available books after Member1 returns one:", lib.list_available_books())
print("Library members:", lib.list_members())
