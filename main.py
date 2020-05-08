
from Games import NoteDifferences
from Games import NotesOnThePiano
from Games import ChordNumberOfScale

from Games import Helpers

import sys, os

if __name__ == "__main__":
  argv = sys.argv[1:]
  notetype = "traditional"
  if len(argv) > 0:
    notetype = argv[0]
    if notetype != "traditional" and notetype != "alphabet":
      print("Note type must be 'traditional' or 'alphabet'")
      sys.exit(0)
    os.environ["MOZARTWILLIAMS"] = notetype

  Helpers.clearTerminal()
  choice = ""
  while choice != "q":
    Helpers.cleanLinesAhead(6)
    print()
    print("1. Note differences")
    print("2. Notes on the piano")
    print("3. Chord number to scale")
    print()

    choice = input("Which game do we play? ")

    if choice == "1":
      game = NoteDifferences.NoteDifferences()
      game.play()
    elif choice == "2":
      game = NotesOnThePiano.NotesOnThePiano()
      game.play()
    elif choice == "3":
      game = ChordNumberOfScale.ChordNumberOfScale()
      game.play()

  # After the lopp
  Helpers.printThanks()
