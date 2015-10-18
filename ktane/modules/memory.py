from ktane import Module
from ktane import CommandLineMixins
from enum import Enum

class Instruction(Enum):
    position = 0
    label = 1

class Memory(Module):
    
    # Display is only valid between 1 and 4
    valid_display = lambda x: 1 <= x <= 4

    # Memory history
    # Dictionary with stage key and an object with [button pressed, its position] as value
    mh = {
      1: {},
      2: {},
      3: {},
      4: {}
      }
    
    # Memory Logic dictionary:
    # Key list is [Stage, Display]
    # Value list is [Instruction, Value]
    ml = {

      # Stage 1
      [1, 1]: [Instruction.position, 2],
      [1, 2]: [Instruction.position, 2],
      [1, 3]: [Instruction.position, 3],
      [1, 4]: [Instruction.position, 4],

      # Stage 2
      [2, 1]: [Instruction.label, 4],
      [2, 2]: [Instruction.position, self.mh[1].position],
      [2, 3]: [Instruction.position, 1],
      [2, 4]: [Instruction.position, self.mh[1].position],

      # Stage 3
      [3, 1]: [Instruction.label, self.mh[2].label],
      [3, 2]: [Instruction.label, self.mh[1].label],
      [3, 3]: [Instruction.position, 3],
      [3, 4]: [Instruction.label, 4],

      # Stage 4
      [4, 1]: [Instruction.position, self.mh[1].position],
      [4, 2]: [Instruction.position, 1],
      [4, 3]: [Instruction.position, self.mh[2].position],
      [4, 4]: [Instruction.position, self.mh[2].position],   
      
      # Stage 5   
      [5, 1]: [Instruction.label, self.mh[1].label],
      [5, 2]: [Instruction.label, self.mh[2].label],
      [5, 3]: [Instruction.label, self.mh[4].label],
      [5, 4]: [Instruction.label, self.mh[3].label],      
      }

    def run(self):
      
      # Logic loop
      for i in range (0,4):
        # Get value in display from user
        display = self.get_display()

        # Tell user which button to press
        answer = self.solve(i, display)
        print(self.humanize(answer))

        # Get necessary information for memory
        stage_info = self.get_stage_info(i, answer)
        self.store(i, stage_info)

    def get_stage_info(self, stage, answer):

      answer_type = answer[0]
      answer_value = answer[1]

      if answer_type == Instruction.label:
        return CommandLineMixins.get_number_or_quit(self, valid_display, 'Which position was that? :')
      else:
        return CommandLineMixins.get_number_or_quit(self, valid_display, 'What was the label? :')

    def solve(self, stage, display):
      return self.ml[stage, display]
       
    # Store data from current stage into memory's history
    def store(self, stage, answer):
      
      self.ml[stage] = {answer[

    # Get valid display value from user
    def get_display(self):
      return CommandLineMixins.get_number_or_quit(self, valid_display, 'Enter the number on the display: ')

    # Humanize instruction
    def humanize(self, instruction):
      if instruction[0] is Instruction.label:
        return 'with the label {}.'.format(instruction[1])
      else:
        return 'in the {}{} position.'.format(instruction[1], ordinalize(instruction[1]))