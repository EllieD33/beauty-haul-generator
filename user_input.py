# Classes related to gathering and processing user inputs.

class UserInputCollector:
    def __init__(self):
        self.responses = {}

    # Ask a single question
    def ask_question(self, question):
        response = input(f"{question}: ")
        self.responses[question] = response
        return response

    # Ask a set of questions
    def collect_inputs(self, questions):
        for question in questions:
            self.ask_question(question)

    # Get responses
    def get_responses(self):
        return self.responses


# Validation class using static methods - add more methods as needed
class InputValidator:
    @staticmethod
    def validate_yes_no(response):
        return response.upper() in ["Y", "N"]
