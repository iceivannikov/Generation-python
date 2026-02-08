import random
from typing import Optional

class MagicBall:
    def __init__(self):
        self.answers = {
            'positive': ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом'],
            'negative': ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно'],
            'neutral': ['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять'],
            'hesitantly_positive': ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
        }

    def _get_random_answer(self):
        answer_type = random.choice(list(self.answers.keys()))
        return random.choice(self.answers[answer_type])

    def ask(self, question: str) -> Optional[str]:
        if question.strip() == '':
            return None
        return self._get_random_answer()

