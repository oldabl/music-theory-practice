
from NoteDictionary import NoteDictionary
import multiprocessing, random

class NoteDifferences:

  def __init__(self):
    self.notes = NoteDictionary().getNotes()
    print("\nWelcome to note differences game!\n")

  def play(self):
    answer = ""
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
      answer = input(question)
      
      if answer in correctnotevariants:
        print("Correct")
      else:
        print("WRONG")
