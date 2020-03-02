def pickle():
    again = 'y'
    output_file = open(FILENAME, 'wb')
    while again.lower() == 'y':
        man = input('Manufacturer: ')
        mod = input('Model: ')
        price = float(input('Price: '))
        phone = ob.CellPhones(man, mod, price)
        pic.dump(phone, output_file)
        again = input('Y? ')
    output_file.close()
    print('Done')


def unpickle():
    end_of_file = False
    file = open(FILENAME, 'rb')
    while not end_of_file:
        try:
            phone = pic.load(file)
            display_data(phone)
        except EOFError:
            end_of_file = True
    file.close()


def display_data(phone):
    print(phone.get_manufacturer())
    print(phone.get_model())
    print(phone.get_price())
    print()

