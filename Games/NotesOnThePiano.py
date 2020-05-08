
import random, os, sys
import Games.Helpers as Helpers

PIANO_ASCII = {
  1: "|   █   █   |   █   █   █   |   █   █   |   █   █   █   |",
  2: "|   █   █   |   █   █   █   |   █   █   |   █   █   █   |",
  3: "|   █   █   |   █   █   █   |   █   █   |   █   █   █   |",
  4: "|   |   |   |   |   |   |   |   |   |   |   |   |   |   |",
  5: "|___|___|___|___|___|___|___|___|___|___|___|___|___|___|",
}
NOTE_SPACE_POSITIONS = {
   0: [(4, 5, 1, 4),(1, 3, 1, 3)],
   1: [(1, 3, 4, 5)],
   2: [(4, 5, 5, 8),(1, 3, 6, 7)],
   3: [(1, 3, 8, 9)],
   4: [(4, 5, 9, 12),(1, 3, 10, 12)],
   5: [(4, 5, 13, 16),(1, 3, 13, 15)],
   6: [(1, 3, 16, 17)],
   7: [(4, 5, 17, 20),(1, 3, 18, 19)],
   8: [(1, 3, 20, 21)],
   9: [(4, 5, 21, 24),(1, 3, 22, 23)],
  10: [(1, 3, 24, 25)],
  11: [(4, 5, 25, 28),(1, 3, 26, 28)],
}
NOTE2_OFFSET = 28

class NotesOnThePiano(Helpers.Game):
  def __init__(self):
    super().__init__()
    print("\nWelcome to notes on the piano game!\n")
    self.notepositions = NOTE_SPACE_POSITIONS


  def printPianoAndNoteSelected(self, notenumber, secondposition, goback):
    if self.notedictionary.isSharp(notenumber):
      pinnotechar = '▒'
    else:
      pinnotechar = '░'

    if goback:
      Helpers.goBackUpLines(5)

    # Print piano with note played
    for (line, value) in PIANO_ASCII.items():
      # Find right coordinates for current line
      (notecoordinatesys, notecoordinatesye, notecoordinatesxs, notecoordinatesxe) = (-1,-1,-1,-1)
      for xy in self.notepositions[notenumber]:
        if xy[0] <= line <= xy[1]:
          (notecoordinatesys, notecoordinatesye, notecoordinatesxs, notecoordinatesxe) = xy
      for position in range(len(value)):
        # Print at right place
        if notecoordinatesxs <= position < notecoordinatesxe:
          sys.stdout.write(pinnotechar)
        else:
          sys.stdout.write(value[position])
      sys.stdout.write("\n")
      sys.stdout.flush()

  
  def play(self):
    answer = ""
    firstround = True

    while answer != "q":
      # Select note number (difficulty handling for sharps to appear)
      notenumber = self.notedictionary.getRandomNoteNumber(includesharp=False)
      if self.score >= 12:
        notenumber = self.notedictionary.getRandomNoteNumber()

      # Will print piano with note chosen
      notesecondposition = random.randint(0, 1)
      self.printPianoAndNoteSelected(notenumber, (notesecondposition==1), (firstround==False))
      Helpers.cleanLinesAhead(1)
      print()

      # Deduct correct answer
      correctnotename = self.notedictionary.getNoteName(notenumber)

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
      firstround = False
    
    # After loop
    self.printBestScore()
