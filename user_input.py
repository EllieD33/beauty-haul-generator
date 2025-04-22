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

    @staticmethod
    def validate_numeric_choices(response, lowest_valid_num, highest_valid_num):
        options = [str(i) for i in range(lowest_valid_num, highest_valid_num + 1)]
        return response in options

    @staticmethod
    def validate_string_choices(response, valid_strings_list):
        options = [i.lower() for i in valid_strings_list]
        return response.lower() in options