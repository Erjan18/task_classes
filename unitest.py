class AnonumousSurvey:
    def __init__(self,question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(f'Ответьте на вопрос: {self.question}')

    def add_answer(self,new_answer):
        self.responses.append(new_answer)

    def show_answers(self):
        for anwser in self.responses:
            print(f'- {anwser}')
question = 'Какой язык программирование самый луший?'
test_poll = AnonumousSurvey(question)
test_poll.add_answer('Phyton')
test_poll.show_answers()