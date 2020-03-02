import os


def main():
    found = False
    search = input('Search for: ')
    new_amo = float(input('New amount: '))
    file = open('file.txt', 'r')
    temp_file = open('temp_file.txt', 'w')
    head = file.readline()
    while head != '':
        amo = float(file.readline())
        head = head.rstrip('\n')
        if head == search:
            temp_file.write(head + '\n')
            temp_file.write(str(new_amo) + '\n')
            found = True
        else:
            temp_file.write(head + '\n')
            temp_file.write(str(amo) + '\n')
        head = file.readline()
    file.close()
    temp_file.close()
    os.remove('file.txt')
    os.rename('temp_file.txt', 'file.txt')
    if found:
        print('Data has been changed!')
    else:
        print("File hasn't been found")


main()