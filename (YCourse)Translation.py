def translate(word):
    translation = ""
    for letter in word:
        if letter in 'AEIOU':
            translation = translation + 'G'
        elif letter in 'aeiou':
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation

print(translate(input('Enter the wordL: ')))