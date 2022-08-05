from abc import ABC, abstractmethod


# task_1
class Person(ABC):
    def __init__(self, name, country, sex):
        self.name = name
        self.country = country
        self.sex = sex
        self.language_know = None

    def __str__(self):
        return f'Name: {self.name}, from: {self.country}, sex: {self.sex}, speaks : {self.language_know} languages'

    @abstractmethod
    def go_to_university(self):
        pass

    @abstractmethod
    def prepere_for_lessons(self):
        pass


class Student(Person):
    def __init__(self, name, country, sex, university):
        super().__init__(name, country, sex)
        self.university = university
        self.language_know = 2

    def go_to_university(self):
        print(f'I go to the {self.university}, to learn myself!')

    def prepere_for_lessons(self):
        print(f' I do all my homework!')


class Teacher(Person):
    def __init__(self, name, country, sex, university, salary, subject):
        super().__init__(name, country, sex)
        self.university = university
        self.salary = salary
        self.subject = subject
        self.language_know = 4

    def go_to_university(self):
        print(f'I go to the {self.university}, to to teach students {self.subject}, and get paid {self.salary}!')

    def prepere_for_lessons(self):
        print(f' Looking for new information to tell students')


#     task_2

class Mathematician:
    @staticmethod
    def square_nums(list_: list):
        return print([i ** 2 for i in list_])

    @staticmethod
    def remove_positives(list_: list):
        return print([i for i in list_ if i < 0])

    @staticmethod
    def filter_leaps(list_: list):
        return print([i for i in list_ if i % 4 == 0])


# task_3
class Product:
    def __init__(self, type_: str, name: str, price: float):
        self.type = type_
        self.name = name
        self.price = price
        self.price_to_sell = round(price * 1.3, 2)
        self.count = 0

    def __str__(self):
        return f' Type: {self.type}, Name: {self.name}, Price:{self.price * 1.3}'

    def __repr__(self):
        return f' Type: {self.type}, Name: {self.name}, Price:{self.price * 1.3}'


cheese = Product("Dairy", "Cheese Brie", 15.9)

pork = Product("Meat", "Pork by weight", 18.0)

choco_bar = Product("Sweats", "Milky Way", 3)


class ProdactStore:
    def __init__(self):
        self.product = Product
        self.store_data = []
        self.income = 0

    def add(self, prod, amount):
        if prod in self.store_data:
            prod.count += amount
            self.income -= prod.price * amount
        else:
            prod.count += amount
            self.income -= prod.price * amount
            self.store_data.append(prod)

    def set_discont(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for prod in self.store_data:
                if prod.name == identifier:
                    prod.price_to_sell = round(prod.price_to_sell * (1 - percent / 100))
                    print(prod.price_to_sell)
        elif identifier_type == 'type':
            for prod in self.store_data:
                if prod.type == identifier:
                    prod.price_to_sell = round(prod.price_to_sell * (1 - percent / 100))

    def sell_product(self, product_name, amount):
        for prod in self.store_data:
            if prod.name == product_name:
                if prod.count < amount:
                    print(f'Not possible to sell, {amount}, only {prod.count} left!')
                else:
                    prod.count -= amount
                    self.income += prod.price_to_sell * amount

    def get_income(self):
        print(self.income)

    def get_all_prodacts(self):
        for prod in self.store_data:
            print(f'{prod.__dict__}')

    def get_product_info(self, product_name):
        for prod in self.store_data:
            if prod.name == product_name:
                print(f'{prod.__dict__}')

#  TASK_4
class CustomExeption(Exception):
    def __init__(self, msg):
        super().__init__((msg))
        with open('Logs.txt','a')as file:
            file.write(msg)





def main():
    # task_1
    # s = Student("Ivan", "UA", "male",'nuft')
    # t = Teacher("Oleg", "UA", "male", "nuft", 8000, "brewing")
    # p = Person("Dmitry","UA", "male")
    # s.go_to_university()
    # print(t.language_know)
    # print(p.__str__())

    #     task_2
    m = Mathematician()

    # m.square_nums([7, 11, 5, 4])
    #
    # m.remove_positives([26, -11, -8, 13, -90])
    #
    # m.filter_leaps([2001, 1884, 1995, 2003, 2020])

    #     task_3
    atb = ProdactStore()

    # atb.add(pork, 5)
    # atb.add(cheese, 45)
    # atb.add(pork, 10)
    # atb.add(pork, 20)
    # atb.add(choco_bar, 99)
    # atb.add(choco_bar, 1)
    # atb.get_income()
    # atb.sell_product('Milky Way', 90)
    # atb.sell_product('Pork by weight', 30)
    # atb.sell_product('Cheese Brie', 30)
    # atb.get_income()
    # atb.set_discont("Dairy", 80, "type")
    # atb.get_all_prodacts()

#     task_4


if __name__ == "__main__":
    main()
