import ob


def main():
    dictionary = {}
    for num in range(1, 5):
        create(dictionary)
    player1 = 0
    player2 = 0
    question_num = 0
    for obj in dictionary:
        question_num += 1
        print(obj)
        answer = int(input('Answer: '))
        if answer == dictionary[obj]:
            if question_num < 3:
                player1 += 1
            else:
                player2 += 1
    if player1 > player2:
        print('Player 1 won! He got ' + str(player1) + 'question right!')
    elif player1 < player2:
        print('Player 2 won! He got ' + str(player2) + 'question right!')
    elif player1 == player2:
        print('Tie!')


def create(dictionary):
    question = input('Write question: ')
    ans1 = input('Answer 1: ')
    ans2 = input('Answer 2: ')
    ans3 = input('Answer 3: ')
    ans4 = input('Answer 4: ')
    right = int(input('Number of correct answer: '))
    quest = ob.Question(question, ans1, ans2, ans3, ans4, right)
    dictionary[quest.get_question()] = quest.get_right_answer()
    return dictionary

