class InstantiateCSVError(Exception):
    def __init__(self):
        self.error = 'Файл item.csv поврежден'

    def __str__(self):
        return self.error


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        """
        Декоратор property.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер обрезающий длину наименования, если она превышает 10 символов.
        """
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name
        return self.__name

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, который принимает путь к документу с значениями.
        Открывает документ и преобразовывает его в словарь.
        Инициализирует значения под атрибуты класса
        """
        import csv
        import os
        cls.all.clear()
        paths = os.path.exists(path)
        if paths == False:
            raise FileNotFoundError('Отсутствует файл item.csv')
        else:
            with open(path, 'r', newline='') as attributes:
                attribute = csv.DictReader(attributes)
                for attr in attribute:
                    if 'name' not in attr:
                        raise InstantiateCSVError
                    name = attr['name']
                    if 'price' not in attr:
                        raise InstantiateCSVError
                    price = cls.string_to_number(attr['price'])
                    if 'quantity' not in attr:
                        raise InstantiateCSVError
                    quantity = cls.string_to_number(attr['quantity'])
                    items_csv = Item(name, price, quantity)
            return items_csv

    @staticmethod
    def string_to_number(string: str):
        """
        Метод принимает строковое значение числа и переводит его в целое число
        """
        if string.isdigit:
            if '.' in string:
                string = int(float(string))
            else:
                string = int(string)
            return string

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """ Магический метод add делает проверку что:
        Экземпляр self относиться к классу self
        Экземпляр other наследуется от класса self """
        if isinstance(self, self.__class__):
            if issubclass(other.__class__, self.__class__):
                return self.quantity + other.quantity
