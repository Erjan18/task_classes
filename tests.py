from unitest import AnonumousSurvey
from unittest import TestCase
class TestAnonumousSurvey(TestCase):
    def test_single_response(self):
        question = 'Какой это автомабиль?'
        new_poll = AnonumousSurvey(question)
        response = 'Бугати'
        new_poll.add_answer(response)
        self.assertIn(response,new_poll.responses)

    def test_list_responses(self):
        question = 'Какой чай вы предологаете?'
        responses = ['Elite','lipton','Акбар','Жемчужина нила']
        new_poll = AnonumousSurvey(question)
        for response in responses:
            new_poll.add_answer(response)
        self.assertEqual(len(responses),len(new_poll.responses))

        self.