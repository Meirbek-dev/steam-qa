class Item(object):
    def __init__(
        self, name: str, release_date: str, platforms, price, review_summary: str
    ):
        self.__name = name
        self.__release_date = release_date
        self.__platforms = platforms
        self.__price = price
        self.__review_summary = review_summary
        self.info = {
            "name": self.name,
            "release date": self.release_date,
            "platforms": self.platforms,
            "price": self.price,
            "review summary": self.review_summary,
        }

    @property
    def name(self):
        return self.__name

    @property
    def release_date(self):
        return self.__release_date

    @property
    def platforms(self):
        return self.__platforms

    @property
    def price(self):
        return self.__price

    @property
    def review_summary(self):
        return self.__review_summary

    @name.setter
    def name(self, value):
        self.__name = value

    @release_date.setter
    def release_date(self, value):
        self.__release_date = value

    @platforms.setter
    def platforms(self, value):
        self.__platforms = value

    @price.setter
    def price(self, value):
        self.__price = value

    @review_summary.setter
    def review_summary(self, value):
        self.__review_summary = value
