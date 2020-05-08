
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

      # Pick movement degree (with difficulty handling)
      movement = random.randint(1, 2 + int(self.score/6))
      tonetype = 1
      if self.score > 17: # include tones
        tonetype = random.randint(1, 2)

      # At high score, starts adding substraction (difficulty handling)
      plusorminus = 1 # addition
      if self.score > 26:
        plusorminus = random.randint(1, 2)

      # Select right operation
      if plusorminus == 1:
        noteshift = movement*tonetype
        operationchar = "+"
      else: # plusorminus == 2
        noteshift = -1*movement*tonetype
        operationchar = "-"

      correctnotenumber = self.notedictionary.getNotePlusSemitonesNumber(notenumber, noteshift)
      correctname = self.notedictionary.getNoteName(correctnotenumber)

      question = self.notedictionary.getNoteName(notenumber)+" "+operationchar+" "+str(movement) + " "
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
