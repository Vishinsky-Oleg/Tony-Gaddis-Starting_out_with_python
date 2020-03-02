
def main():
    price = int(input('Price of item: '))
    ftax = fed_tax(price)
    rtax = reg_tax(price)
    print('Price of purchase: ', price)
    print('Federal tax (2,5%): ', ftax)
    print('Regional tax (5%): ', rtax)
    print('Both tax\'s: ', ftax + rtax)
    print('Sum of purchase: ', ftax + rtax + price)


def fed_tax(num):
    return num * 0.025


def reg_tax(num):
    return num * 0.05


main()