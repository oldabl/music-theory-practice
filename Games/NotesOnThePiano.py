
import random, os
from Games.NoteDictionary import NoteDictionary

PIANO_ASCII = """
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
"""
PIANO_WIDTH = 57
NOTE_SPACE_POSITIONS = {
  0: ("C" , 2),
  1: ("C#", 5),
  2: ("D" , 6),
  3: ("D#", 9),
  4: ("E" , 10),
  5: ("F" , 14),
  6: ("F#", 17),
  7: ("G" , 18),
  8: ("G#", 21),
  9: ("A" , 22),
  10:("A#", 25),
  11:("B" , 26),
}
NOTE2_OFFSET = 28

class NotesOnThePiano:
  def __init__(self):
    self.notes = NoteDictionary().getNotes()
    print("\nWelcome to notes on the piano game!\n")
    print(PIANO_ASCII)
    self.addExtraPositions()
  
  def addExtraPositions(self):
    self.notePositions = dict()
    for (key, value) in NOTE_SPACE_POSITIONS.items():
      self.notePositions[key] = (value[0], value[1], value[1]+NOTE2_OFFSET)
  
  def play(self):
    answer = ""
    firstround = True
    width = os.get_terminal_size()[0]
    while answer != "q":
      notenumber = random.randint(0, 23)
      correctnoteposition = self.notePositions[notenumber%12]
      correctnote = self.notes[notenumber%12]
      pinnotechar = "^"
      if correctnoteposition[1]%2 == 0:
        pinnotechar = "^^"
      notespace = correctnoteposition[1]-1
      if notenumber >= 12:
        notespace = correctnoteposition[2]
      if firstround:
        firstround = False
        uptwolines = ""
      else:
        firstround = False
        uptwolines = "\033[F\033[F\033[F\n"+" "*width+"\033[F"
      print(uptwolines+notespace*" "+pinnotechar+" "*(PIANO_WIDTH-len(notespace*" "+pinnotechar)))
      answer = input("What's this note? ")
      if answer in self.notes[notenumber%12]:
        print(width*" "+"\rCORRECT, it was a "+correctnote[1])
      else:
        print(width*" "+"\rWRONG, correct note was "+correctnote[1])
