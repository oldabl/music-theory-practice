
import random
import Games.Helpers as Helpers

class NoteDifferences:

  def __init__(self):
    Helpers.clearTerminal()
    self.notes = Helpers.NoteDictionary().getNotes()
    print("\nWelcome to note differences game!")

  def play(self):
    answer = ""
    
    inarow = 0
    bestscore = 0

    while answer != "q":
      notenumber = random.randint(0, 11)
      movement = random.randint(1, 2)
      tones = random.randint(1, 2)
      correctanswer = (notenumber + movement*tones) % len(self.notes)
      correctnotevariants = self.notes[correctanswer]

      question = self.notes[notenumber][1]+" + "+str(movement) + " "
      if tones == 1:
        question += "semiton"
      else: #if tones == 2
        question += "ton"
      if movement > 1:
        question += "s"
      question += " = "
      answer = input("\n"+question)
      
      if answer in correctnotevariants:
        inarow += 1
        print("Correct! "+str(inarow)+" in a row! It was indeed a "+correctnotevariants[1])
      else:
        inarow = 0
        print("WRONG! Actually it was a "+correctnotevariants[1])
      
      # Update best score
      if inarow > bestscore:
        bestscore = inarow
    
    # After loop
    print("\nBest score was: "+str(bestscore))
    Helpers.printThanks()

