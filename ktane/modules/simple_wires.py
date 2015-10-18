from enum import Enum
from ktane import Module
from collections import Counter
from inflection import ordinalize

class Color(Enum):
    white = 1
    red = 2
    blue = 3
    yellow = 4
    black = 5

class SimpleWires(Module):

    def run(self):
        # Get wires from user
        wire_strings = self.get_list_or_quit(
            lambda x: x.lower() in Color.__members__.keys(), 
            range(3, 7), 
            'Input wire colors separated by a space.')

        # If our input test returned None, the user is quitting.  Else, continue
        if wire_strings == None:
            return

        self.wires = list(map(lambda x: Color[x.lower()], wire_strings))
        self.color_counts = Counter(self.wires)

        # Fire the correct method depending on number of wires
        wire_num = {
            3: self.three,
            4: self.four,
            5: self.five,
            6: self.six,
        }[len(self.wires)]()

        if wire_num is None:
            return

        self.output_and_wait(
            'Cut the {} wire', 
            [ordinalize(wire_num), 'last'][wire_num == len(self.wires)])

    def three(self):
        # Logic 3-1
        if not Color.red in self.wires:
            return 2

        # Logic 3-2
        if self.wires[-1] == Color.white:
            return len(self.wires)

        # Logic 3-3
        if self.color_counts[Color.blue] > 1:
            return len(self.wires) - self.wires[::-1].index(Color.blue)

        # Logic 3-4
        return len(self.wires)

    def four(self):
        # Logic 4-1
        if self.color_counts[Color.red] > 1:
            odd_digit = self.__get_last_digit_odd()
            if odd_digit is None:
                return None
            if odd_digit:
                return len(self.wires) - self.wires[::-1].index(Color.red)

        # Logic 4-2
        if self.wires[-1] == Color.yellow and self.color_counts[Color.red] == 0:
            return 1

        # Logic 4-3
        if self.color_counts[Color.blue] == 1:
            return 1

        # Logic 4-4
        if self.color_counts[Color.yellow] > 1:
            return len(self.wires)

        # Logic 4-5
        return 2

    def five(self):
        # Logic 5-1
        if self.wires[-1] == Color.black:
            odd_digit = self.__get_last_digit_odd()
            if odd_digit is None:
                return None
            if odd_digit:
                return 4

        # Logic 5-2
        if self.color_counts[Color.red] == 1 and self.color_counts[Color.yellow] > 1:
            return 1

        # Logic 5-3
        if self.color_counts[Color.black] == 0:
            return 2

        # Logic 5-4
        return 1

    def six(self):
        # Logic 6-1
        if self.color_counts[Color.yellow] == 0:
            odd_digit = self.__get_last_digit_odd()
            if odd_digit is None:
                return None
            if odd_digit:
                return 4

        # Logic 6-2
        if self.color_counts[Color.yellow] == 1 and self.color_counts[Color.white] > 1:
            return 4

        # Logic 6-3
        if self.color_counts[Color.red] == 0:
            return len(self.wires)

        # Logic 6-4
        return 4

    def __get_last_digit_odd(self):
        digit = self.get_number_or_quit(
            lambda x: x in range(10),
            'Input the last digit of the serial number.')
        return None if digit is None else digit % 2 != 0
