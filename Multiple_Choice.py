class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "What is the color a red car?\n(a) Red\n(b) Blue\n(c) Yellow\n\n",
    "What is the color of a blue car?\n(a) Red\n(b) Blue\n(c) Yellow\n\n",
    "What is the color of a yellow car?\n(a) Red\n(b) Blue\n(c) Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")

]


def run_test(x):
    score = 0
    for question in x:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(x)) + " correct.")


run_test(questions)
