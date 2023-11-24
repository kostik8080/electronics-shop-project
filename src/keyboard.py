from src import item


class LanguageMixin:
    """
    Mixin class for managing and changing the keyboard layout language.
    """
    LANGUAGES = ['EN', 'RU']

    def __init__(self):


        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value in self.LANGUAGES:
            self.__language = value
        else:
            raise ValueError(f"Unsupported language: {value}")

    def change_lang(self):
        """
        Toggles the keyboard layout language between the available languages.
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'







class Keyboard(item.Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
