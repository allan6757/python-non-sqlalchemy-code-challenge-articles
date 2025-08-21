class Article:
    all = []

    def __init__(self, author, magazine, title):
        # validate title
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters")
        
        self._title = title
        self.author = author
        self.magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title