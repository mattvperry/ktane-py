from ktane import Module
from ktane import CommandLineMixins
from enum import Enum
from inflection import ordinalize

class Logic():
  def __init__(self, instruction, value):
    self.instruction = instruction
    self.value = value

class Instruction(Enum):
    position = 0
    label = 1

class Memory(Module):
    
    # Display is only valid between 1 and 4
    valid_display = lambda x: 1 <= x <= 4

    # Memory history
    # Dictionary with stage key and an object with [button pressed, its position] as value
    mh = {
      1: None,
      2: None,
      3: None,
      4: None
      }
    
    # Memory Logic dictionary:
    # Key list is [Stage, Display]
    # Value list is [Instruction, Value]
    def get_logic(self, stage):
      if stage == 1:
        return {
          # Stage 1
          1: Logic(Instruction.position, 2),
          2: Logic(Instruction.position, 2),
          3: Logic(Instruction.position, 3),
          4: Logic(Instruction.position, 4),
        }
      elif stage == 2:
        return {
          # Stage 2
          1: Logic(Instruction.label, 4),
          2: Logic(Instruction.position, self.mh[1][1]),
          3: Logic(Instruction.position, 1),
          4: Logic(Instruction.position, self.mh[1][1]),
        }
      elif stage == 3:
        return {
          # Stage 3
          1: Logic(Instruction.label, self.mh[2][0]),
          2: Logic(Instruction.label, self.mh[1][0]),
          3: Logic(Instruction.position, 3),
          4: Logic(Instruction.label, 4),
        }
      elif stage == 4:
        return {
          # Stage 4
          1: Logic(Instruction.position, self.mh[1][1]),
          2: Logic(Instruction.position, 1),
          3: Logic(Instruction.position, self.mh[2][1]),
          4: Logic(Instruction.position, self.mh[2][1]),   
        }
      elif stage == 5:
        return {
          # Stage 5   
          1: Logic(Instruction.label, self.mh[1][0]),
          2: Logic(Instruction.label, self.mh[2][0]),
          3: Logic(Instruction.label, self.mh[4][0]),
          4: Logic(Instruction.label, self.mh[3][0]),      
        }
      else:
        return None

    def run(self):
      
      # Logic loop
      for i in range (1,6):

        # Print stage label
        print('\nStage {}\n----------'.format(i))

        # Get value in display from user
        display = self.get_display()

        # Tell user which button to press
        answer = self.solve(i, display)
        print('\nPress the button {}\n'.format(self.humanize(answer)))

        # Get necessary information for memory
        stage_info = self.get_stage_info(i, answer)
        self.store(i, answer, stage_info)

      input('Press Enter key to exit...')
      return

    def get_stage_info(self, stage, answer):

      answer_type = answer.instruction
      answer_value = answer.value

      if answer_type == Instruction.label:
        return self.get_number_or_quit(
          lambda x: 1 <= x <= 4, 
          'Which position was that? :')
      else:
        return self.get_number_or_quit(
          lambda x: 1 <= x <= 4, 
          'What was the label? :')

    def solve(self, stage, display):
      return self.get_logic(stage)[display]
       
    # Store data from current stage into memory's history
    def store(self, stage, answer, instruction):
      if instruction == Instruction.label:
        self.mh[stage] = (answer.value, stage)
      else:
        self.mh[stage] = (stage, answer.value)

    # Get valid display value from user
    def get_display(self):
      return self.get_number_or_quit(
        lambda x: 1 <= x <= 4, 
        'Enter the number on the display: ')

    # Humanize instruction
    def humanize(self, answer):
      if answer.instruction == Instruction.label:
        return 'with the label {}.'.format(answer.value)
      else:
        return 'in the {} position.'.format(ordinalize(answer.value))