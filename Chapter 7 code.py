import random


def sales():
    list = []
    sum = 0
    index = 0
    for num in range(1,8):
        list.append(int(input('Sales in day #' + str(num) + ': ')))
        sum += list[index]
        index += 1
    print(sum)


def rand():
    list = []
    for num in range(7):
        list.append(random.randint(0, 9))
        print(list[num], end='')


def precipitation():
    months = {
        '0': 'January',
        '1': 'February',
        '2': 'March',
        '3': 'April',
        '4': 'May',
        '5': 'June',
        '6': 'July',
        '7': 'August',
        '8': 'September',
        '9': 'October',
        '10': 'November',
        '11': 'December',
    }
    list = []
    sum = 0

    for mon in range(12):
        precip = input('Precipitation in ' + months[str(mon)] + ': ')
        list.append(int(precip))
        sum += list[mon]
    avg = sum / 12
    print('Summary is: ', sum)
    print('Average is: ', format(avg, '.2f'))
    print('Minimal in ' + months[str(list.index(min(list)))] + ': ', min(list))
    print('Maximum in ' + months[str(list.index(max(list)))] + ': ', max(list))


def numbers():
    sum = 0
    list = []
    for num in range(20):
        list.append(int(input('Number ' + str(num + 1) + ': ')))
        sum += list[num]
    print(sum)
    print(sum / 20)
    print(min(list))
    print(max(list))


def accounts():
    file = open('file.txt', 'r')
    list = file.readlines()
    look = int(input('Looking for: '))
    for el in range(len(list)):
        list[el] = int(list[el].rstrip('\n'))
    if look in list:
        print('Correct:')
    else:
        print('Incorrect')
    file.close()


def biggerThanN():
    list = [15, 78, 15, 97, 8, 5]
    n = 33
    for num in list:
        if num > n:
            print(num)


def test():
    taken_list = take_test()
    file = open('file.txt', 'r')
    check_list = file.readlines()
    right = 0
    file.close()
    wrong_list = []
    for n in range(20):
        check_list[n] = check_list[n].rstrip('\n')
        if check_list[n] == taken_list[n]:
            right += 1
        else:
            wrong_list.append(str(n + 1) + ' : ' + taken_list[n])
    print()
    if right >= 15:
        print('You past the test')
        print('Wrong answers:')
        for el in wrong_list:
            print(el)
    else:
        print('You failed')
        print('Wrong aswers:')
        for el in wrong_list:
            print(el)
def take_test():
    num = 1
    list = []
    for t in range(20):
        list.append(input('Answer to question #' + str(num) + ': '))
        num += 1
    return list


def pop_name():
    file =open('file.txt', 'r')
    list = file.readlines()
    name = input('Name: ')
    for n in range(len(list)):
        list[n] = list[n].rstrip('\n')
    if name in list:
        print('Popular')
    else:
        print('Not popular')
    file.close()


def population():
    file = open('file.txt', 'r')
    list = file.readlines()
    list_of_change = []
    list_of_years = []
    year = 1950
    first = 0
    second = 1
    total = 0
    for num in range(len(list)):
        list[num] = list[num].rstrip('\n')
        list[num] = int(list[num])
    for y in range(1, 41):
        list_of_change.append(list[second] - list[first])
        total += list[second] - list[first]
        year += 1
        list_of_years.append(year)
        first += 1
        second += 1
    file.close()
    print('Average human population grow: ', int(total / 40))
    print('Maximum in', list_of_years[list_of_change.index(max(list_of_change))], 'year: ', max(list_of_change))
    print('Minimum in', list_of_years[list_of_change.index(min(list_of_change))], 'year: ', min(list_of_change))


def world_cup():
    file = open('file.txt', 'r')
    team = input('Team: ')
    years = create_years()
    win_list = []
    team_list = file.readlines()
    for t in range(len(team_list)):
        team_list[t] = team_list[t].rstrip('\n')
        if team_list[t] == team:
            win_list.append(years[t])
    print('Your team winned ' + str(len(win_list)) + ' times in following years: ')
    print(win_list)
def create_years():
    list1 = []
    for y in range(1903, 2010):
        if y != 1904 and y != 1994:
            list1.append(y)
    return list1


def lo_chu_sq():
    lo_chu = [
        [4, 9, 2],
        [3, 5, 7],
        [8, 1, 6]
    ]
    check(lo_chu)
def check(list):
    r1, r2, r3, c1, c2, c3, d1, d2 = 0, 0, 0, 0, 0, 0, 0, 0
    for r in range(3):
        r1 += list[0][r]
        r2 += list[1][r]
        r3 += list[2][r]
        c1 += list[r][0]
        c2 += list[r][1]
        c3 += list[r][2]
    d1 = list[0][0] + list[1][1] + list[2][2]
    d2 = list[0][2] + list[1][1] + list[2][0]
    if r1 == r2 and r1 == r2 and r1 == r3 and r1 == c1 and r1 == c2 and r1 == c3 and r1 == d1 and r1 == d2:
        print('LO CHU SQUARE!')
    else:
        print('Wrong')


def prime_number():
    look = int(input('Checking number: '))
    list = check_prime_nums(look)
    print(list)
    if look in list:
        print('Prime number!')
    else:
        print('Wrong')
def check_prime_nums(num):
    prime_nums = []
    for num in range(1, num + 1):
        if num > 1:

            # Iterate from 2 to n / 2
            for i in range(2, num // 2):

                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(int(num))
    return prime_nums


def magic_ball():
    file = open('file.txt', 'r')
    list = file.readlines()
    go_on = 'y'
    for n in range(len(list)):
        list[n] = list[n].rstrip('\n')
    while go_on == 'y':
        input('Ask your question: ')
        print(list[random.randint(0, len(list) - 1)])
        go_on = input('Continue y?: ')


