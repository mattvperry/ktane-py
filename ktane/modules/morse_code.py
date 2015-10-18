from ktane import Module

class MorseCode(Module):

    frequencies = {
        "shell": 505,
        "halls": 515,
        "slick": 522,
        "trick": 532,
        "boxes": 535,
        "leaks": 542,
        "strobe": 545,
        "bistro": 552,
        "flick": 555,
        "bombs": 565,
        "break": 572,
        "brick": 575,
        "steak": 582,
        "sting": 592,
        "vector": 595,
        "beats": 600
    }

    morse_lookup = {
        ".-"    : "a",
        "-..."  : "b",
        "-.-."  : "c",
        "-.."   : "d",
        "."     : "e",
        "..-."  : "f",
        "--."   : "g",
        "...."  : "h",
        ".."    : "i",
        ".---"  : "j",
        "-.-"   : "k",
        ".-.."  : "l",
        "--"    : "m",
        "-."    : "n",
        "---"   : "o",
        ".--."  : "p",
        "--.-"  : "q",
        ".-."   : "r",
        "..."   : "s",
        "-"     : "t",
        "..-"   : "u",
        "...-"  : "v",
        ".--"   : "w",
        "-..-"  : "x",
        "-.--"  : "y",
        "--.."  : "z",
    }
    
    def run(self):
        answer = self.stream_solve(
            self.__get_morse_or_quit,
            lambda cs: [v for k, v in self.frequencies.items() if cs in (k + k)])
        if answer is None:
            return

        self.output_and_wait("Respond at frequency: 3.{} MHz", answer)

    def __get_morse_or_quit(self):
        morse_chars = self.get_list_or_quit(
            lambda x: x in self.morse_lookup.keys(), 
            range(1, 7), 
            'Enter morse characters seperated by a space.')
        if morse_chars is None:
            return None

        return ''.join([self.morse_lookup[x] for x in morse_chars])