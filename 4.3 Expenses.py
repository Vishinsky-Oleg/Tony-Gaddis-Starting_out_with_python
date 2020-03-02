
spent = 0
exp_it_g = []
item_g = []
proceed = 'y'
budget = int(input('Enter your budget for month: '))
print('--------------------------')
while proceed == 'y':
    exp_it = str(input('Enter expense item: '))
    exp_it_g.append(exp_it)
    item = int(input('Enter expense: '))
    item_g.append(item)
    proceed = str(input('Do you wish to proceed y/n: '))
else:
    print()
    for ex in range(len(exp_it_g)):
        print('You spend:', item_g[int(ex)], 'on: ', exp_it_g[int(ex)])
        spent += item_g[int(ex)]
    if spent == budget:
        print('Total spent is', spent, '. You spent your budget even.')
    elif spent < budget:
        print('Total spent is', spent, '. You saved ', budget - spent)
    else:
        print('Total spent is', spent, '. You expend ', spent - budget)
