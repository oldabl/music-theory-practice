
import random, os, sys
import Games.Helpers as Helpers

PIANO_ASCII = """
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|"""
PIANO_WIDTH = 57
NOTE_SPACE_POSITIONS = {
   0:  2,
   1:  4,
   2:  6,
   3:  8,
   4: 10,
   5: 14,
   6: 16,
   7: 18,
   8: 20,
   9: 22,
  10: 24,
  11: 26,
}
NOTE2_OFFSET = 28

class NotesOnThePiano(Helpers.Game):
  def __init__(self):
    super().__init__()
    print("\nWelcome to notes on the piano game!\n")
    self.addExtraPositions()
  
  def addExtraPositions(self):
    self.notePositions = dict()
    for (key, value) in NOTE_SPACE_POSITIONS.items():
      self.notePositions[key] = value
      self.notePositions[key+len(NOTE_SPACE_POSITIONS)] = value+NOTE2_OFFSET
  
  def play(self):
    print(PIANO_ASCII)

    answer = ""

    while answer != "q":
      notenumber = self.notedictionary.getRandomNoteNumber(includesharp=False)
      if self.score > 12:
        notenumber = self.notedictionary.getRandomNoteNumber()

      notesecondposition = random.randint(0, 1)

      correctanswernoteposition = self.notePositions[notenumber] + notesecondposition * NOTE2_OFFSET
      correctnotename = self.notedictionary.getNoteName(notenumber)

      pinnotechar = '^'

      Helpers.cleanLinesAhead(1)
      print(correctanswernoteposition*" "+pinnotechar)

      # Let player play
      Helpers.cleanLinesAhead(1)
      answer = input("What's this note? ")
      Helpers.cleanLinesAhead(1)

      if self.notedictionary.doesStringMatchNoteNumber(Helpers.noAccentsOrSpaces(answer), notenumber):
        self.handleScore(True)
        print("Correct! "+str(self.score)+" in a row! It was indeed a "+correctnotename)
      else:
        self.handleScore(False)
        print("WRONG! Actually it was a "+correctnotename)
      
      Helpers.goBackUpLines(3)
    
    # After loop
    self.printBestScore()
