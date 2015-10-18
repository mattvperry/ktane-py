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
        answer = self.solve()
        if answer is None:
            return

        self.output_and_wait("The answer is: {}", answer)

    def solve(self):
        for chars in self.__get_char_stream():
            if chars is None:
                return None
            words = self.words
            columns = self.__chunk_six(chars)
            for i, col in enumerate(columns):
                words = [word for word in words if word[i] in col]
            if len(words) == 1:
                return words[0]

    def __get_char_stream(self):
        inputs = ""
        while True:
            chars = self.get_string_or_quit(
                range(6, 31),
                'Enter up to 30 characters.')
            if chars is None:
                yield None
            else:
                inputs += chars
                yield inputs

    def __chunk_six(self, chars):
        return [chars[i:i + 6] for i in range(0, len(chars), 6)]