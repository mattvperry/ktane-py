from ktane import Module

class SimpleWires(Module):
    def run(self):
      print('Running Simple Wires Module...')
   
      # Define colors
      colors = {'white', 'red', 'blue', 'yellow', 'black'}
      print ('Simple Wires\n----------\n')
      numWires = int(input('How many wires? : '))
      wires = [None for x in range(numWires)]
      for wireNum in range(0,numWires) :
        wires[wireNum] = input('Wire ' + str(wireNum + 1) + ' color? : ')

      def cut(wireNum):
        print('Cut wire number %d' % wireNum)
        return

      def three(wires):
        # Logic 3-1
        if not any("red" in s for s in wires):
          cut(2)
  
        # Logic 3-2
        elif wires[len(wires) - 1] == "white":
          cut(len(wires))
  
        # Logic 3-3
        elif wires.count("blue") > 1:
          cut(len(wires) - wires[::-1].index("blue"))

        # Logic 3-4
        else:
          cut(len(wires))

      def four(wires):
        # Logic 4-1
        # Todo: Get serial #
        serialNum = "AE4293"

        if wires.count('red') > 1 and int(serialNum[5]) % 2 == 1:
          cut(len(wires) - wires[::-1].index("red"))

        # Logic 4-2
        elif wires[len(wires) - 1] == 'yellow' and wires.count('red') == 0:
          cut(1)

        # Logic 4-3
        elif wires.count("blue") == 1:
          cut(1)

        # Logic 4-4
        elif wires.count("yellow") > 1:
          cut(len(wires))

        # Logic 4-5
        else:
          cut(2)
 
      def five(wires):
        # Logic 5-1
        # Todo: Get serial #
        serialNum = "AE4293"

        if wires[len(wires - 1)] == "black" and int(serialNum[5]) % 2 == 1:
          cut(4)

        # Logic 5-2
        elif wires.count("red") == 1 and wires.count("yellow") > 1:
          cut(1)

        # Logic 5-3
        elif wires.count("black") == 0:
          cut(2)

        # Logic 5-4
        else:
          cut(1)

      def six(wires):
        # Logic 6-1
        if wires.count("yellow") == 0 and int(serialNum[6]) % 2 == 1:
          cut(4)

        # Logic 6-2
        elif wires.count("yellow") == 1 and wires.count("white") > 1:
          cut(4)

        # Logic 6-3
        elif wires.count("red") == 0:
          cut(len(wires))

        # Logic 6-4
        else:
          cut(4)
 
      # User input => function dictionary
      moduleType = {
        3: three,
        4: four,
        5: five,
        6: six,
      }
      
      moduleType[numWires](wires)