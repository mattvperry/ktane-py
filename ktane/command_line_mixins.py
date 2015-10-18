import os

class CommandLineMixins(object):
    def get_choice_or_quit(self, choices):
        [print('{}. {}'.format(i + 1, x)) for (i, x) in enumerate(sorted(choices))]
        print()
        choice = self.get_number_or_quit(
            lambda x: x in range(1, len(choices) + 1),
            "Select a module")
        return None if choice is None else choices[choice - 1]

    def get_list_or_quit(self, validator, length_range, message):
        def list_validator(str):
            list = str.split(' ')
            valid_entries = all([validator(x) for x in list])
            valid_length = len(list) in length_range
            return valid_entries and valid_length

        list = self.get_valid_input_or_quit(list_validator, message)
        return None if list is None else list.split(' ')

    def get_number_or_quit(self, validator, message):
        user_input = self.get_valid_input_or_quit(
            lambda x: x.isdigit() and validator(int(x)), 
            message)
        return None if user_input is None else int(user_input)

    def get_string_or_quit(self, length_range, message):
        return self.get_valid_input_or_quit(
            lambda x: x.isalpha() and len(x) in length_range, 
            message)

    def get_valid_input_or_quit(self, validator, message):
        user_input = input('{} (q to quit):\n'.format(message))
        while user_input.lower() != 'q' and not validator(user_input):
            user_input = input("Invalid input. Try again:\n")
        return None if user_input.lower() == 'q' else user_input

    def cls(self):
        os.system(['clear', 'cls'][os.name == 'nt'])