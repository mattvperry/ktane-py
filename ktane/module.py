from ktane import CommandLineMixins

class Module(CommandLineMixins):

    def stream_solve(self, get_chars_or_quit, solve):
        for chars in self.__get_char_stream(get_chars_or_quit):
            if chars is None:
                return None
            solutions = solve(chars)
            if len(solutions) == 1:
                return solutions[0]

    def output_and_wait(self, message, *args):
        print()
        print(message.format(*args))
        print()
        input('Press enter to continue...')

    def __get_char_stream(self, get_chars_or_quit):
        chars = ""
        while True:
            char = get_chars_or_quit()
            if char is None:
                yield None
            else:
                chars += char
                yield chars