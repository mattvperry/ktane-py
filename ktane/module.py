from ktane import CommandLineMixins

class Module(CommandLineMixins):

    def output_and_wait(self, message, *args):
        print()
        print(message.format(*args))
        print()
        input('Press enter to continue...')