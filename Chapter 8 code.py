
def f_i_o():
    word = input('Word:')
    full = word.split(' ')
    fio = ''
    for name in full:
        fio += name[0].upper() + '.'
    print(fio)


def sum():
    try:
        num = int(input('Num: '))
        summary = 0
        for each in str(num):
            summary += int(each)
        print(summary)
    except ValueError:
        print('Numbers!')
        sum()


def date():
    months = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }
    dat = input('Date: ')
    validation(dat)
    if validation(dat):
        date_inputed = dat.split('/')
        print(date_inputed[0] + ' ' + months[date_inputed[1]] + ' ' + date_inputed[2] + ' y.')
    else:
        print('Format: xx/xx/xxxx. Try again!')
        date()
def validation(word):
    valid = False
    word = str(word)
    valid_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    valid_days = []
    for num in range(1,32):
        valid_days.append(str(num))
    if word[:2].isdigit() and word[2] == '/' and word[3:5].isdigit() and word[5] == '/' and word[6:10].isdigit():
        if word[:2] in valid_days and word[3:5] in valid_months:
            valid = True
    else:
        valid = False
    return valid


def morse_code():
    word = input('Word:')
    morse_word = ''
    for l in word:
        if l == ' ':
            morse_word += l
        if l == ',':
            morse_word += '--..--'
        if l == '.':
            morse_word += '.-.-.-'
        if l == '?':
            morse_word += '..--..'
        if l.isdigit():
            if l == '0':
                morse_word += '-----'
            if l == '1':
                morse_word += '.----'
            if l == '2':
                morse_word += '..---'
            if l == '3':
                morse_word += '...--'
            if l == '4':
                morse_word += '....-'
            if l == '5':
                morse_word += '.....'
            if l == '6':
                morse_word += '-....'
            if l == '7':
                morse_word += '--...'
            if l == '8':
                morse_word += '---..'
            if l == '9':
                morse_word += '----.'
        if l.isalpha():
            if l.upper() == 'A':
                morse_word += '.-'
            # ONLY UNTIL A
    print(morse_word)


def phone_number():
    list = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z']
    ]
    word = input('Word:')
    number = ''
    for l in word:
        if l.isdigit() or l == '-':
            number += l
        for each in range(8):
            if l.upper() in list[each]:
                number += str(each + 2)
    print(number)


def average_words():
    words = 1
    sum = 0
    num_of_sent = 1
    num_of_words = []
    file = open('file.txt', 'r')
    sentenses = file.readlines()
    for num in range(len(sentenses)):
        sentenses[num] = sentenses[num].rstrip('\n')
    for sent in sentenses:
        for l in sent:
            if l.isspace():
                words +=1
        num_of_words.append(words)
        words = 1
    for lenght in num_of_words:
        sum += lenght
        print('In sent #' + str(num_of_sent) + ': ' + str(lenght) + ' words.')
        num_of_sent += 1
    print('Average is: ' + format(sum / len(sentenses), '.1f'))
    file.close()


def first_letters():
    original = input('Sentence: ')
    mutated = ''
    capitalize = True
    list_of_words = original.split(' ')
    for word in list_of_words:
        for letter in word:
            if capitalize:
                mutated += letter.upper()
                capitalize = False
            else:
                mutated += letter
            if letter == '.' or letter == '!' or letter == '?':
                capitalize = True
        mutated += ' '
    print(mutated)


def vowels_consonants():
    original = input('Sentence: ')

    consonants = 'BCDFGHJKLMNPQRSTVXZY'
    num_of_cons = 0
    vowels = 'AEIOU'
    num_of_vow = 0
    for let in original:
        if let.upper() in consonants:
            num_of_cons += 1
        if let.upper() in vowels:
            num_of_vow += 1
    print('Num on cons: ' + str(num_of_cons) + '\n' + 'Num of vow: ' + str(num_of_vow))


def word_divider():
    original = input('Sentence: ')
    first = True
    mutated = ''
    for let in original:
        if first:
            mutated += let.upper()
            first = False

        else:
            if let.isupper():
                mutated += ' ' + let.lower()
            else:
                mutated += let
    print(mutated)


def youth_jargon():
    original = input('Sentence: ')
    list_of_words = original.split(' ')
    mutated = ''
    for word in list_of_words:
        mutated += word[1:] + word[0] + 'shit' + ' '
    print(mutated)









