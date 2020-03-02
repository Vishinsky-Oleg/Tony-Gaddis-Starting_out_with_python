import pickle as pkl


def preserve():
    again = 'y'
    outputfile = open('file.dat', 'wb')
    while again.lower() == 'y':
        save_data(outputfile)
        again = input('Continue: ')
    outputfile.close()


def save_data(file):
    person = {}
    person['Name: '] = input('Name')
    person['Age: '] = int(input('Age: '))
    person['Mass: '] = int(input('Mass: '))
    pkl.dump(person, file)


def open_up():
    file = open('file.dat', 'rb')
    end = False
    while not end:
        try:
            person = pkl.load(file)
            display_data(person)
            print()
        except EOFError:
            end = True

    file.close()


def display_data(person):
    for e in person:
        print(e + ' : ' + str(person[e]))




