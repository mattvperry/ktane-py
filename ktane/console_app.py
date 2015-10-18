from pyfiglet import Figlet
from ktane import Module, CommandLineMixins
from ktane.modules import *
from inflection import titleize

class ConsoleApp(CommandLineMixins):
    def __init__(self):
        self.ascii = Figlet(font='standard')
        self.modules = self.__get_module_dict()

    def start(self):
        while True:
            print(self.ascii.renderText('KTANE SOLVER'))
            choice = self.get_choice_or_quit(list(self.modules.keys()))
            if choice is None:
                break
            self.cls()
            print(self.ascii.renderText(choice))
            self.modules[choice].run()
            self.cls()

    def __get_module_dict(self):
        return { titleize(klass.__name__): klass() for klass in Module.__subclasses__() }