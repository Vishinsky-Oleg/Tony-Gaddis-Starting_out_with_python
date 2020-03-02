
days = int(input('Input amount of days: '))
payrate = 1

print('Day\t\tPay Rate')
for day in range(days):
    print(day + 1, '\t\t', payrate)
    payrate = payrate * 2
print('After ', days, 'your pay rate will be: ', payrate / 100)