
kph = int(input('Type-in the speed: '))
kpm = kph / 60
time = int(input('Type-in minutes: '))
hours = time // 60

print('Hours\tDistance traveled')
for hour in range(hours):
    print(hour + 1, '\t', (hour + 1) * kph)

if time % 60 != 0:
    print(time // 60, 'h.', time % 60, 'm.', '\t', format(time * kpm, '.1f'))