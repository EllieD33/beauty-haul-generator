# Classes related to gathering and processing user inputs.

class UserInputCollector:
    # Ask a single question
    @staticmethod
    def ask_question(question):
        response = input(f"{question}: ")
        return response


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
        options = [i.lower().strip() for i in valid_strings_list]
        return response.lower().strip() in options

    @staticmethod
    def validate_complete_numeric_ranking(response, lowest_valid_num, highest_valid_num):
        cleaned_response = response.replace(",", " ")
        user_numbers = set(cleaned_response.strip().split())

        expected_numbers = {str(i) for i in range(lowest_valid_num, highest_valid_num + 1)}

        return user_numbers == expected_numbers
