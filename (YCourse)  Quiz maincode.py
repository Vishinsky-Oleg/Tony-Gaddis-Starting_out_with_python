class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "Color of apples?\n(a) Green\n(b) Yellow\n(c) Orange\n\n",
    "Color of bananas?\n(a) Blue\n(b) Red\n(c) Yellow\n\n",
    "Color of tomatoes?\n(a) Red\n(b) Blue\n(c) Orange\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a")
]




def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got ", str(score), "/", str(len(questions)), ' correct')

run_test(questions)



