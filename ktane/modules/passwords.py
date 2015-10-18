from ktane import Module

class Passwords(Module):

    words = ['about', 'after', 'again', 'below', 'could', 
             'every', 'first', 'found', 'great', 'house', 
             'large', 'learn', 'never', 'other', 'place', 
             'plant', 'point', 'right', 'small', 'sound', 
             'spell', 'still', 'study', 'their', 'there', 
             'these', 'thing', 'think', 'three', 'water', 
             'where', 'which', 'world', 'would', 'write']

    def run(self):
        answer = self.stream_solve(self.__get_chars_or_quit, self.__solve)
        if answer is None:
            return

        self.output_and_wait("The answer is: {}", answer)

    def __get_chars_or_quit(self):
        return self.get_string_or_quit(range(6, 31), 'Enter up to 30 characters.')

    def __solve(self, chars):
        words = self.words
        columns = self.__chunk_six(chars)
        for i, col in enumerate(columns):
            words = [word for word in words if word[i] in col]
        return words

    def __chunk_six(self, chars):
        return [chars[i:i + 6] for i in range(0, len(chars), 6)]