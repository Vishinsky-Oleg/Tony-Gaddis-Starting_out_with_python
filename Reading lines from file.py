

def main():
    sales_file = open('sales.txt', 'r')
    line = sales_file.readline()
    while line != '':
        amount = float(line)
        print(format(amount, '.2f'))
        line = sales_file.readline()
    sales_file.close()


main()



#WRITE 3 Lines!!!!!!!!!



def main():
    sales = open('sales.txt', 'w')
    amount = int(input('Enter amount: '))
    for man in range(1, amount+1):
        name = input('Name:')
        id = int(input('Id:'))
        saled = float(input('Saled:'))
        sales.write(str(name) + '\n')
        sales.write(str(id) + '\n')
        sales.write(str(saled) + '\n')
    print('Data has been reseived!')
    sales.close()


main()


#READ 3 Lines!!!!!!!!!



def main():
    file = open('sales.txt', 'r')
    name = str(file.readline())
    while name != '':
        id = str(file.readline())
        saled = str(file.readline())
        print('Name: ' + name + 'Id: ' + id + 'Saled: ' + saled)
        name = str(file.readline())
    file.close()

main()



