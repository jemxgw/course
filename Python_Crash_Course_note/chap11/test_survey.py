import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        question = 'What language did you first learn to speak?'
        self.responses = ['chinese', 'english', 'japanese']
        self.survey = AnonymousSurvey(question)

    def test_store_single_response(self):
        self.survey.store_response(self.responses[0])
        self.assertIn('chinese', self.survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)

unittest.main()
