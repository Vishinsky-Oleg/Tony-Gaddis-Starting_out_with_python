import ob
import pickle as pic


# FILENAME = 'cellphones.dat'
FILENAME = 'contacts.dat'
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
def dictionary_class():
    mycontacts = load_contacts()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    save_contacts(mycontacts)
def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        contact_dict = pic.load(input_file)
        input_file.close()
    except IOError:
        contact_dict = {}
    return contact_dict
def get_menu_choice():
    print()
    print('Menu')
    print('---------------')
    print('1. Contacts\n2. Add\n3.Change\n4.Delete\n5.QUIT')
    print()
    choice = int(input('Choose: '))
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Choose correctly: '))
    return choice
def look_up(mycontacts):
    name = input('Name look: ')
    print(mycontacts.get(name, 'There is no such name!'))
def add(mycontacts):
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    entry = ob.Contact(name, phone, email)
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Added')
    else:
        print('Already there')
def change(mycontacts):
    name = input('Name: ')
    if name in mycontacts:
        phone = input('New phone num: ')
        email = input('New email: ')
        entry = ob.Contact(name, phone, email)
        mycontacts[name] = entry
        print('Updated')
    else:
        print('404 Name not found')
def delete(mycontacts):
    name = input('Name: ')
    if name in mycontacts:
        del mycontacts[name]
        print('Deleted')
    else:
        print('404 Name not found')
def save_contacts(mycontacts):
    output_file = open(FILENAME, 'wb')
    pic.dump(mycontacts, output_file)
    output_file.close()


