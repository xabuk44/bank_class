class Book:
    def __init__(self, name,author,tag):
        self.name = name
        self.author = author
        self.tag = tag


container = []
container.append(Book('War and Piece', 'Tolstoy', ['love', 'train']))
container.append(Book('Return from the stars', 'Stanislav Lem', ['future']))


def search_by_name(container, name):
    result = []
    for book in container:
        if name in book.name:
            result.append(book)
        return result

def filter_by_name(container, name):
    return list(filter(lambda book: name in book.name, container))
