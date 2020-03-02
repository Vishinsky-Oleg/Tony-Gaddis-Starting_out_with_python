import random
def steps_write():
    file = open('file.txt', 'w')
    for num in range(1, 366):
        file.write(str(random.randint(15, 200)) + '\n')
    file.close()


def app():
    file = open('file.txt', 'r')
    daym = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31
    ]
    month = 0
    for m in range(12):
        amount = 0
        for d in range(1, daym[month] + 1):
            amount += int(file.readline())
        print(amount // daym[month])
        month += 1
    print('Done')
    file.close()



###WORKS!!!!!!!!!!!:
def app1():
    file = open('file.txt', 'r')
    amount = 0
    for j in range(1, 32):
        amount += int(file.readline())
    print(amount // 31)
    amount = 0
    for f in range(1, 29):
        amount += int(file.readline())
    print(amount // 28)
    amount = 0
    for m in range(1, 32):
        amount += int(file.readline())
    print(amount // 31)
    amount = 0
    for a in range(1, 31):
        amount += int(file.readline())
    print(amount // 30)
    amount = 0
    for ma in range(1, 32):
        amount += int(file.readline())
    print(amount // 31)
    amount = 0
    for ju in range(1, 31):
        amount += int(file.readline())
    print(amount // 30)
    amount = 0
    for jul in range(1, 32):
        amount += int(file.readline())
    print(amount // 31)
    amount = 0
    for au in range(1, 32):
        amount += int(file.readline())
    print(amount // 31)
    amount = 0
    for s in range(1, 31):
        amount += int(file.readline())
    print(amount // 30)
    amount = 0
    for o in range(1, 32):
        amount += int(file.readline())
    print(amount // 31)
    amount = 0
    for n in range(1, 31):
        amount += int(file.readline())
    print(amount // 30)
    amount = 0
    for d in range(1, 32):
        amount += int(file.readline())
    print(amount // 31)
    file.close()