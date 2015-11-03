from enum import Enum
from ktane import Module


class Color(Enum):
    white = 1
    blue = 2
    red = 3
    yellow = 4


class Text(Enum):
    detonate = 1
    hold = 2
    abort = 3


class Indicator(Enum):
    SND = 1
    CLR = 2
    CAR = 3
    IND = 4
    FRQ = 5
    SIG = 6
    NSA = 7
    MSA = 8
    TRN = 9
    BOB = 10
    FRK = 11


# Module for "The Button". The logic for lit indicators
# and batteries is likely better placed outside of this
# class and into a more general space.
# Quitting in the middle of an event is also not functional because you can't
# correctly unravel the stack with that input unless you account for it
# with every function call (which defeats the purpose).
class Buttons(Module):

    # Number of Batteries
    batteries = -1

    # Lit indicators
    lit_indicators = ['None']

    # Entry point for the module
    def run(self):

        # Reset Number of Batteries
        self.batteries = -1

        # Reset Lit indicators
        self.lit_indicators = ['None']

        # Get the button
        color = Color[self.get_valid_input_or_quit(
            lambda x: x.lower() in Color.__members__.keys(),
            "Enter the color of the button: ")]

        text = Text[self.get_valid_input_or_quit(
            lambda x: x.lower() in Text.__members__.keys(),
            "Enter the button text: ")]

        self.output_and_wait(self.apply_logic(color, text))

    # Function to apply the logic for solving the button based on inputs
    def apply_logic(self, color, text):
        # Case 1
        if (color is Color.blue and text is Text.abort):
            return self.hold()

        # Case 2
        if (text is Text.detonate and self.get_batteries() > 1):
            return self.press_and_release()

        # Case 3
        if (color is Color.white and "CAR" in self.get_lit_indicators()):
            return self.hold()

        # Case 4
        if (self.get_batteries() > 2 and "FRK" in self.get_lit_indicators()):
            return self.press_and_release()

        # Case 5
        if (color is Color.yellow):
            return self.hold()

        # Case 6
        if (color is Color.red and text is Text.hold):
            return self.press_and_release()

        # Case 7
        return self.hold()

    # Press and release
    def press_and_release(self):
        return "Press and immediately release the button"

    def hold(self):
        print ('\nHold the button...\n')
        stripe = Color[self.get_valid_input_or_quit(
            lambda x: x.lower() in Color.__members__.keys(),
            "Enter the color of the the stripe: ")]

        return "Release when the timer has a {} in any position".format(self.get_stripe_number(stripe))

    # Function to get countdown timer number from stripe color
    def get_stripe_number(self, stripe):
        if (stripe is Color.blue):
            return 4
        elif (stripe is Color.yellow):
            return 5
        else:
            return 1

    # Function to get number of batteries from user
    def get_batteries(self):
        if (self.batteries is -1):
            batts = self.get_number_or_quit(
                lambda x: x >= 0,
                "Enter number of batteries: "
                )
            self.batteries = batts
            return self.batteries
        else:
            return self.batteries

    # Function to get list of lit indicators from user
    def get_lit_indicators(self):
        if (self.lit_indicators[0] is 'None'):
            indics = [x.upper() for x in self.get_list_or_quit(
                lambda x: x.upper() in Indicator.__members__.keys(),
                range(0, 99),
                "Enter all lit indicators separated by spaces: "
                )]
            self.lit_indicators = indics
            return self.lit_indicators
        else:
            return self.lit_indicators
