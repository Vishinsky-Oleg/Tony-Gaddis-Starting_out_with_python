def read_from_file():
    file = open('file.txt', 'r')
    list1 = file.readlines()
    index = 0
    while index < len(list1):
        list1[index] = int(list1[index])
        index += 1
    file.close()
    print(list1)


def write_to_file():
    file = open('file.txt', 'w')
    list = [1, 2, 3, 5, 7, 9]
    for n in list:
        file.write(str(n) + '\n')
    file.close()


read_from_file()
