from ktane import Module

class SimpleWires(Module):

    def run(self):
      # Setup 'Simple Wires' display
      self.clear()
      print('Running Simple Wires Module...\n')
   
      # Define colors
      colors = {'white', 'red', 'blue', 'yellow', 'black'}
      
      # Get wires from user
      wires = input('input wire colors separated by a space. Enter q to quit\n').split(' ')
      numWires = len(wires)

      # Kick out if our wire list is too short or long or if we have any invalid wires
      if not 3 <= len(wires) <= 6 or False in map(lambda w: w in colors, wires):
        self.run()
        return

      # Fire the correct method depending on number of wires
      self.moduleType[numWires](self,wires)

    def cut(self,wireNum):
      suffix = {1:"st",2:"nd",3:"rd",4:"th",5:"th",6:"th"}

      print('\nCut the {}{} wire\n'.format(wireNum, suffix[wireNum]))
      return

    def three(self,wires):
      # Logic 3-1
      if not any("red" in w for w in wires):
        self.cut(2)
  
      # Logic 3-2
      elif wires[len(wires) - 1] == "white":
        self.cut(len(wires))
  
      # Logic 3-3
      elif wires.count("blue") > 1:
        self.cut(len(wires) - wires[::-1].index("blue"))

      # Logic 3-4
      else:
        self.cut(len(wires))

    def four(self,wires):
      # Logic 4-1
      # Todo: Get serial #
      serialNum = "AE4293"

      if wires.count('red') > 1 and int(serialNum[5]) % 2 == 1:
        self.cut(len(wires) - wires[::-1].index("red"))

      # Logic 4-2
      elif wires[len(wires) - 1] == 'yellow' and wires.count('red') == 0:
        self.cut(1)

      # Logic 4-3
      elif wires.count("blue") == 1:
        self.cut(1)

      # Logic 4-4
      elif wires.count("yellow") > 1:
        self.cut(len(wires))

      # Logic 4-5
      else:
        self.cut(2)
 
    def five(self,wires):
      # Logic 5-1
      # Todo: Get serial #
      serialNum = "AE4293"

      if wires[len(wires - 1)] == "black" and int(serialNum[5]) % 2 == 1:
        self.cut(4)

      # Logic 5-2
      elif wires.count("red") == 1 and wires.count("yellow") > 1:
        self.cut(1)

      # Logic 5-3
      elif wires.count("black") == 0:
        self.cut(2)

      # Logic 5-4
      else:
        self.cut(1)

    def six(self,wires):
      # Logic 6-1
      if wires.count("yellow") == 0 and int(serialNum[6]) % 2 == 1:
        self.cut(4)

      # Logic 6-2
      elif wires.count("yellow") == 1 and wires.count("white") > 1:
        self.cut(4)

      # Logic 6-3
      elif wires.count("red") == 0:
        self.cut(len(wires))

      # Logic 6-4
      else:
        self.cut(4)
 
    # User input => function dictionary
    moduleType = {
      3: three,
      4: four,
      5: five,
      6: six,
    }