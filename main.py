
from NoteDifferences import NoteDifferences

if __name__ == "__main__":
  print("1. Note differences")
  choice = input("Which game do we play? ")
  if choice == "1":
    notediff = NoteDifferences()
    notediff.play()
  else:
    print("No game chosen, will quit")