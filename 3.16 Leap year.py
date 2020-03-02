num = int(input('Input year: '))

if num % 100 == 0 and num % 400 == 0:
    print('Leap year!')
else:
    if num % 100 != 0 and num % 4 == 0:
        print('Leap year!')
    else:
        print('Not leap year!')