
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
  0: ("C" , 2),
  1: ("C#", 4),
  2: ("D" , 6),
  3: ("D#", 8),
  4: ("E" , 10),
  5: ("F" , 14),
  6: ("F#", 16),
  7: ("G" , 18),
  8: ("G#", 20),
  9: ("A" , 22),
  10:("A#", 24),
  11:("B" , 26),
}
NOTE2_OFFSET = 28

class NotesOnThePiano:
  def __init__(self):
    Helpers.clearTerminal()
    self.notes = Helpers.NoteDictionary().getNotes()
    print("\nWelcome to notes on the piano game!\n")
    print(PIANO_ASCII)
    self.addExtraPositions()
  
  def addExtraPositions(self):
    self.notePositions = dict()
    for (key, value) in NOTE_SPACE_POSITIONS.items():
      self.notePositions[key] = value
      self.notePositions[key+len(self.notes)] = (value[0], value[1]+NOTE2_OFFSET)
  
  def play(self):
    answer = ""
    firstround = True

    # Line clean string
    linecleanstring = " "*os.get_terminal_size()[0]+"\r"

    # Keep track
    inarow = 0
    bestscore = 0

    while answer != "q":
      notenumber = random.randint(0, len(self.notePositions)-1)

      correctnoteposition = self.notePositions[notenumber]
      correctnote = self.notes[notenumber%12]

      # If not sharp, double pointing char
      pinnotechars = ('^', '∣')

      # Check if has to erase 2 last lines
      if firstround:
        firstround = False
        comebackthreelines = ""
        reservespaceafterquestion = "\n"*2+"\033[F\033[F"
      else:
        firstround = False
        comebackthreelines = "\033[F\033[F\033[F\033[F"
        reservespaceafterquestion = ""

      sys.stdout.write(comebackthreelines)
      sys.stdout.flush()


      sys.stdout.write(linecleanstring+"\n"+linecleanstring+"\033[F") # To wipe line clean
      sys.stdout.write(correctnoteposition[1]*" "+pinnotechars[0]+"\n")
      sys.stdout.write(correctnoteposition[1]*" "+pinnotechars[1]+"\n")
      sys.stdout.flush()

      # Let player play
      sys.stdout.write(reservespaceafterquestion+linecleanstring) # To wipe line clean
      sys.stdout.flush()
      answer = input("What's this note? ")

      sys.stdout.write(linecleanstring) # To wipe line clean
      sys.stdout.flush()
      if answer in correctnote:
        inarow += 1
        print("Correct! "+str(inarow)+" in a row! It was indeed a "+correctnote[1])
      else:
        inarow = 0
        print("WRONG! Actually it was a "+correctnote[1])

      # Update best score
      if inarow > bestscore:
        bestscore = inarow
    
    # After loop
    print("\nBest score was: "+str(bestscore))
    Helpers.printThanks()

