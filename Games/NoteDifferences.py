
import random
import Games.Helpers as Helpers

class NoteDifferences(Helpers.Game):

  def __init__(self):
    super().__init__()
    print("\nWelcome to note differences game!")

  def play(self):
    answer = ""

    while answer != "q":
      notenumber = self.notedictionary.getRandomNoteNumber()

      movement = random.randint(1, 2 + int(self.score/6))
      tonetype = random.randint(1, 2)

      # At high score, starts adding substraction
      plusorminus = 1 # addition
      if self.score > 20:
        plusorminus = random.randint(1, 2)

      if plusorminus == 1:
        noteshift = movement*tonetype
        addchar = "+"
      else: # plusorminus == 2
        noteshift = -1*movement*tonetype
        addchar = "-"

      correctnotenumber = self.notedictionary.getNotePlusSemitonesNumber(notenumber, noteshift)
      correctname = self.notedictionary.getNoteName(correctnotenumber)

      question = self.notedictionary.getNoteName(notenumber)+" "+addchar+" "+str(movement) + " "
      if tonetype == 1:
        question += "semitone"
      else: #if tonetype == 2
        question += "tone"
      if movement > 1:
        question += "s"
      question += " = "
      answer = input("\n"+question)
      
      if self.notedictionary.doesStringMatchNoteNumber(Helpers.noAccentsOrSpaces(answer), correctnotenumber):
        self.handleScore(True)
        print("Correct! "+str(self.score)+" in a row! It was indeed a "+correctname)
      else:
        self.handleScore(False)
        print("WRONG! Actually it was a "+correctname)
    
    # After loop
    self.printBestScore()
