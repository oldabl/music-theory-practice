
from Games import NoteDifferences
from Games import NotesOnThePiano

if __name__ == "__main__":
  print("1. Note differences")
  print("2. Notes on the piano")
  choice = input("Which game do we play? ")
  if choice == "1":
    game = NoteDifferences.NoteDifferences()
    game.play()
  elif choice == "2":
    game = NotesOnThePiano.NotesOnThePiano()
    game.play()
  else:
    print("No game chosen, will quit")
