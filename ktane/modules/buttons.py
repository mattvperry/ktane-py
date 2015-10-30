from ktane import Module
from ktane import command_line_mixins

class Color(Enum):
    white = 1
    blue = 2
    red = 3
    yellow = 4

class Text(Enum):
    detonate = 1
    hold = 2
    abort = 3

class Buttons(Module):

    def run(self):
      # Get the button
      button = self.get_list_or_quit(
        lambda x: x.lower() in self.Color.__members__.Keys() or x.lower() in self.Text.__members__.Keys(),
        range(3, 9),
        "Enter the button color and the button text separated by a space.")
      # Check if our button is valid
      if button[0].lower() not in self.Color.__members__.Keys() or button[1].lower() not in self.Text.__members__.Keys():
        print "Invalid button entered."
        return



    def get_batteries(self):
      batteries = self.get_number_or_quit(
        )