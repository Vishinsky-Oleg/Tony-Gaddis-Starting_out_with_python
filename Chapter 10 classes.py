class CellPhones:
    def __init__(self, manufac, model, price):
        self.__manufacturer = manufac
        self.__model = model
        self.__price = price

    def set_manufacturer(self, manufact):
        self.__manufacturer = manufact

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price


class Bank:
    def __init__(self, amount):
        self.__amount = amount

    def deposit(self, amount):
        self.__amount += amount

    def withdraw(self, amount):
        if amount <= self.__amount:
            self.__amount -= amount
        else:
            print('Not enough')

    def get_balance(self):
        return self.__amount

    def __str__(self):
        return 'some text' + format(self.__amount, '.2f')


class Contact:
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def __str__(self):
        return 'Name: ' + self.__name + \
              '\nPhone: ' + self.__phone + \
              '\nEmail: ' + self.__email


class Pet:
    def __init__(self, name, type, age):
        self.__name = name
        self.__type = type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_type(self, type):
        self.__name = type

    def set_age(self, age):
        self.__name = age

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_age(self):
        return self.__age


class Car:
    def __init__(self, name, make):
        self.__name = name
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


class Patient:
    def __init__(self, full_name, address, number, emergency_contact):
        self.__name = full_name
        self.__address = address
        self.__number = number
        self.__emergency = emergency_contact

    # Mutator
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address


class RetailItem:
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price


class CashRegister:
    def __init__(self):
        self.__list = []

    def purchase_item(self, item):
        self.__list.append(item)

    def get_total(self):
        total = 0
        for item in self.__list:
            total += item.get_price()
        return total

    def show_items(self):
        for item in self.__list:
            print(item.get_description())
            print(item.get_units())
            print(item.get_price())
            print()

    def clear(self):
        self.__list.clear()

    def get_len(self):
        return len(self.__list)


class Question:
    def __init__(self, question, ans1, ans2, ans3, ans4, right_ans):
        self.__question = question
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__right_ans = right_ans

    def get_question(self):
        return self.__question + '\n' + '1: ' + self.__ans1 + '\n' + '2: ' + self.__ans2 + '\n' + '3: ' + self.__ans3 \
               + '\n' + '4: ' + self.__ans4 + '\n'

    def get_right_answer(self):
        return self.__right_ans




