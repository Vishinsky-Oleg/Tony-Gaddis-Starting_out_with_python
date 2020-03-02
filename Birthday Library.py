#global variables
LOOK_UP = 0
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    birthdays = {}
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)


def get_menu_choice():
    print()
    print('Friend\' birthdays')
    print('-------------------')
    print('1. Find birthday')
    print('2. Add new birthday')
    print('3. Change birthday date')
    print('4. Delete birthday date')
    print('5. Quit program')
    print()
    choice = int(input('Make a choice: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Make a choice: '))
    return choice


def look_up(birthdays):
    name = input('Input name: ')
    print(birthdays.get(name, 'Не найдено'))


def add(birthdays):
    name = input('Input name: ')
    bday = input('Input date: ')
    if name not in birthdays:
        birthdays[name] = bday
    else:
        print('Already exist!')


def change(birthdays):
    name = input('Input name: ')
    if name in birthdays:
        bday = input('Input new date: ')
        birthdays[name] = bday
    else:
        print('Name wasn\'t found')


def delete(birthdays):
    name = input('Input name: ')
    if name in birthdays:
        del birthdays[name]
    else:
        print('Name wasn\'t found')


main()