class Asset:
    def __init__(self,title,on_loan,date_acquired):
        self._title=title
        self._loan=on_loan
        self._date=date_acquired
    def set_loan(self):
        self._loan=True
    def return_loan(self):
        self._loan=False
class Book(Asset):
    def __init__(self, title, on_loan, date_acquired,author,isbn):
        super().__init__(title, on_loan, date_acquired)
        self._isbn=isbn
        self._author=author
    def display(self):
        super().display
        print(f'ISBN:{self._isbn},Author:{self._author}')
class CD(Asset):
    def display(self):
        super().display
        print(f'Artist:{self._artist},Playing time{self._playing_time}')

