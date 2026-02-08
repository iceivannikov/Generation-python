from game.magic_ball.magic_ball import MagicBall

EMPTY_QUESTION_MESSAGE = 'Я всё ещё жду'
EXIT_COMMAND = 'выход'

class Runner:
    def __init__(self, magic_ball):
        self.ball = magic_ball

    def play(self):
        while True:
            question = input('Назови свой вопрос ')
            if question.lower().strip() == EXIT_COMMAND:
                break
            answer = self.ball.ask(question)
            if answer is None:
                print(EMPTY_QUESTION_MESSAGE)
                continue
            else:
                print(answer)


if __name__ == "__main__":
    ball = MagicBall()
    game = Runner(ball)
    game.play()
