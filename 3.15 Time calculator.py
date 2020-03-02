num = int(input('Type seconds: '))


if num <= 60:
    print("It's just ", num, ' seconds.')
else:
    if num <= 3600:
        print("It's ", num // 60, ' minutes and ', num % 60, ' seconds.')
    else:
        if num <= 86400:
            print("It's ", num // 3600, ' hours and ', num % 3600 // 60, ' minutes and ', num % 3600 % 60, ' seconds.')
        else:
            print("It's ", num // 86400, ' days and ', num % 86400 // 3600, ' hours and ', num % 86400 % 3600 // 60, ' minutes and ', num % 86400 % 3600 % 60, ' seconds.')