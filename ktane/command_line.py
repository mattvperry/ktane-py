from ktane import Module
from ktane.modules import *
from inflection import humanize, underscore

def main():
    modules = __get_module_dict()
    while True:
        choice = get_choice(list(modules.keys()))
        if choice is None:
            break
        modules[choice].run()

def get_choice(choices):
    [print('{}. {}'.format(i + 1, x)) for (i, x) in enumerate(choices)]
    choice = get_number_or_quit(
        lambda x: x > 0 and x <= len(choices),
        "Select a module")
    return None if choice is None else choices[choice - 1]

def get_number_or_quit(validator, message):
    user_input = get_valid_input_or_quit(
        lambda x: x.isdigit() and validator(int(x)), 
        message)
    return None if user_input is None else int(user_input)

def get_valid_input_or_quit(validator, message):
    user_input = input('{} (q to quit):\n'.format(message))
    while user_input != 'q' and not validator(user_input):
        user_input = input("Invalid input. Try again:\n")
    return None if user_input == 'q' else user_input

def __get_module_dict():
    return { __humanize_class_name(klass): klass() for klass in Module.__subclasses__() }

def __humanize_class_name(klass):
    return humanize(underscore(klass.__name__))