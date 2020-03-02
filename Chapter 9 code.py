def course_number():
    dict = {
        'CS101': [3004, 'Hynes', '8:00'],
        'CS102': [4501, 'Alvarado', '9:00'],
        'CS103': [6755, 'Rich', '10:00'],
        'NT110': [1244, 'Byrk', '11:00'],
        'CM241': [1411, 'Lee', '13:00']
    }
    name = input('Number: ')



    list = dict[name]
    for i in list:
        print(i)


def dictionary():
    right_asnwer = 0
    capitals = {
        'USA': 'Washington',
        'Russia': 'Moscow',
        'China': 'Beiging',
        'Ukraine': 'Kiev',
        'Uzbekistan': 'Tashkent',
        'Beloruss': 'Minsk'
    }
    for key in capitals:
        print(key)
        value = input('Input value: ')
        if value == capitals[key]:
            print('Good!')
            right_asnwer += 1
        else:
            print('Bad!')
    print(str(right_asnwer) + ' out of ' + str(len(capitals)))


coding = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
}
def main():
    file = open('file.txt', 'r')
    full_text = ''
    text = file.readlines()
    for i in text:
        full_text += i
    code(full_text)
    file.close()
    print(full_text)
def code(text):
    file = open('file1.txt', 'w')
    for each in text:
        if each in coding:
            file.write(coding[each])
        elif each == ' ':
            file.write(' ')
        elif each == '\n':
            file.write('\n')
    file.close()
def decode():
    file = open('file1.txt', 'r')
    decoded = ''
    text = file.readlines()
    for l in text:
        for q in l:
            for k, y in coding.items():
                if q == y:
                    decoded += k
            if q == ' ':
                decoded += ' '
            if q == '\n':
                decoded += '\n'
    print(decoded)
    file.close()


def file_into_text(file):
    text = ''
    lines = file.readlines()
    for element in lines:
        for let in element:
            if let == '\n':
                text += ' '
            else:
                text += let
    file.close()
    return text
def unique():
    list = file_into_text().split(' ')
    old_set = set(list)
    print(old_set)


def frequency():
    freq_dict = {}
    list_of_words = file_into_text().split()
    for word in list_of_words:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    print(freq_dict)


def world_series_winners():
    year = int(input('Year: '))

    years_dict = dict_with_years()
    win_count_dic = win_count()
    if year in years_dict:
        print(str(year) + ' : ' + years_dict[year] + ' : ' + str(win_count_dic[years_dict[year]]))
def dict_with_years():
    file = open('file.txt', 'r')
    dict = {}
    year = 1903
    lines = file.readlines()
    for line in lines:
        line = line.rstrip('\n')
        if year != 1904 and year != 1994:
            dict[year] = line
        year += 1
    file.close()
    return dict
def win_count():
    file = open('file.txt', 'r')
    dict = {}
    lines = file.readlines()
    for line in lines:
        line = line.rstrip('\n')
        if line not in dict:
            dict[line] = 1
        else:
            dict[line] += 1
    file.close()
    return dict


import pickle
FIND = 1
ADD = 2
CHANGE = 3
DEL = 4
QUIT_n_SAVE = 5
def email_dict():
    try:
        old_dict = open_preserved()
        print(old_dict)
    except FileNotFoundError:
        print('File isn\'t there yet!')

    dict = {}
    CHOSEN = 0
    while CHOSEN != QUIT_n_SAVE:
        CHOSEN = menu()
        if CHOSEN == 1:
            find_ed(dict)
        if CHOSEN == 2:
            add_ed(dict)
        if CHOSEN == 3:
            change_ed(dict)
        if CHOSEN == 4:
            del_ed(dict)
        print()
    else:
        preserve(dict)
def menu():
    print('1 find')
    print('2 add')
    print('3 change')
    print('4 del')
    print('5 qns')
    print()
    choice = int(input('Make a choice: '))
    while choice < FIND or choice > QUIT_n_SAVE:
        choice = int(input('Make a choice: '))
    return choice
def find_ed(dict):
    name = input('Name you want to find: ')
    if name in dict:
        print('Email: ' + dict[name])
    else:
        print('Name hasn\'t been found')
    return dict
def add_ed(dict):
    name = input('Name you want to add: ')
    email = input('Email: ')
    if name not in dict:
        dict[name] = email
        print('Name has been added!')
    else:
        print('Already there')

    return dict
def change_ed(dict):
    name = input('Name you want to change: ')
    email = input('New Email: ')
    if name in dict:
        dict[name] = email
        print('Name changed')
    else:
        print('Name hasn\'t been found')
    return dict
def del_ed(dict):
    name = input('Name you want to delete: ')
    if name in dict:
        del dict[name]
        print('Deleted')
    else:
        print('Not there')
def preserve(dict):
    file = open('file.dat', 'wb')
    pickle.dump(dict, file)
    file.close()
def open_preserved():
    dict = {}
    file = open('file.dat', 'rb')
    end = False
    while not end:
        try:
            name = pickle.load(file)
            for k in name:
                dict[k] = name[k]
        except EOFError:
            end = True
    file.close()
    return dict

email_dict()