class Book:
    """
    Represents a book in a library system.
    
    Attributes
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    year : int
        The publication year of the book.
    """
    
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance.
        
        Parameters
        ----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        year : int
            The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self) -> str:
        """
        Return a string representation of the book.
        
        Returns
        -------
        str
            Formatted string with book details.
        """
        return f'"{self.title}" by {self.author} ({self.year})'
    
    def get_age(self) -> int:
        """
        Calculate the age of the book assuming the current year is 2025.
        
        Returns
        -------
        int
            The age of the book in years.
        """
        return 2025 - self.year

    def read(self) -> str:
        """
        Simulate reading the book.
        
        Returns
        -------
        str
            A string indicating the book is being read.
        """
        return f"Reading '{self.title}'"

class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    
    Attributes
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    year : int
        The publication year of the book.
    file_size : float
        The file size of the ebook in MB.
    """
    
    def __init__(self, title: str, author: str, year: int, file_size: float):
        """
        Initialize an EBook instance.
        
        Parameters
        ----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        year : int
            The publication year of the book.
        file_size : float
            The file size of the ebook in MB.
        """
        # Use super() to call the parent class (Book) constructor
        # This initializes title, author, and year without duplicating code
        super().__init__(title, author, year)
        self.file_size = file_size
        
    def __str__(self) -> str:
        """
        Return a string representation of the ebook.
        
        Returns
        -------
        str
            Formatted string with ebook details and file size.
        """
        # Use super() to call the parent class (Book) __str__ method
        # Then append the EBook-specific file_size information
        return f'{super().__str__()} [Size: {self.file_size}MB]'

    def read(self) -> str:
        """
        Simulate reading the ebook, extending the parent method.
        
        Returns
        -------
        str
            A string indicating the ebook is being read on a device.
        """
        # Call the parent's read() method and extend its functionality
        base_read = super().read()
        return f"{base_read} on an electronic device."

if __name__ == "__main__":
    # Create a Book instance
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
    # Print the book
    print(book1)
    print(f"Age: {book1.get_age()} years")
    print(book1.read())
    
    # Create an EBook instance
    ebook1 = EBook("1984", "George Orwell", 1949, 2.5)
    
    # Print the ebook
    print(ebook1)
    print(f"Age: {ebook1.get_age()} years")
    print(ebook1.read())