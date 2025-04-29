from routine_display import RoutineDisplay, SaveRoutine
from routine_generator import RoutineGenerator
from ui.loading_spinner import Spinner
from user_interactions import UserInputCollector, UserFeedbackCollector, UserPreferenceCollector


def main():
    # Display welcome screen
    UserFeedbackCollector.welcome_user()

    # Set up input collector and feedback collector
    input_collector = UserInputCollector()
    feedback_collector = UserFeedbackCollector(input_collector)
    preference_collector = UserPreferenceCollector(input_collector)

    if not feedback_collector.get_user_consent():
        return

    while True:
        # Get user's preferences
        user_responses = preference_collector.collect_all_preferences()

        # Wraps API calls in the spinner UI - spinner indicates loading state
        app_spinner = Spinner(message="Generating your beauty haul")
        app_spinner.start()
        try:
            routine_generator = RoutineGenerator(user_responses)
            routine = routine_generator.generate_routine()
        finally:
            app_spinner.stop()

        routine_display = RoutineDisplay(routine, user_responses)

        # Display output functions
        routine_display.check_if_routine_empty()
        if routine:
            routine_display.display_title()
            routine_display.display_routine()

        # Check if user is satisfied with recommended routine
        if feedback_collector.is_user_satisfied():
            routine_saver = SaveRoutine(routine)
            routine_saver.save_routine()
            print("Thank you for using the beauty generator, you're glowing with your new routine! ✨")
            break
        else:
            print("Don't worry, lets start again!✨")


if __name__ == "__main__":
    main()
