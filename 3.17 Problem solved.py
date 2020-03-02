print('Restart your Pc and try to reconnect')
solve = str(input('Problem solved y/n: '))
solved = False

while solved != True:
    if solve == "n":
        print('Q1')
        solve = str(input('Problem solved y/n: '))
        if solve == "n":
            print('Q2')
            solve = str(input('Problem solved y/n: '))
            if solve == "n":
                print('Q3')
                solve = str(input('Problem solved y/n: '))
    else:
        solved = True