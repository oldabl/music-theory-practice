
import random
import Games.Helpers as Helpers

# Game difficulty
#maxsemitones = 24 (2 octaves)
# -> maxtones = 24/2 = 12
#semitones = 2+difficulty/6
#maxdifficulty = (24-2)*6 = 132
class NoteDifferences(Helpers.Game):

  def __init__(self):
    super().__init__()
    print("\nWelcome to note differences game!")
    self.setMaxDifficulty(132)

  def play(self):
    answer = ""

    self.printQuitInfo()
    while answer != self.endGameString:
      # Pick random note to start with
      if self.ratioMaxDifficulty(4):
        #Use sharps at high difficulty
        notenumber = self.notedictionary.getRandomNoteNumber()
      else:
        #Don't use sharps at low difficulty
        notenumber = self.notedictionary.getRandomNoteNumber(False)

      # Pick number of semitones to put on top
      semitonesnumber = random.randint(1, int(2 + self.difficulty/6))
      if self.ratioMaxDifficulty(3):
        #Include tones at high difficulty
        tonetype = random.randint(1, 2)
      else:
        #Only use semitones
        tonetype = 1

      # Pick addition or substraction
      if self.ratioMaxDifficulty(2):
        #Include substraction at high difficulty
        plusorminus = random.randint(1, 2)
      else:
        #Addition only
        plusorminus = 1

      # Prepare variables for question
      if plusorminus == 1: # Addition
        noteshift = semitonesnumber
        operationchar = "+"
      else: # Substraction
        noteshift = -1*semitonesnumber
        operationchar = "-"
      # Remove (semi)tones trailing 0 if there is one
      questiontones = semitonesnumber/tonetype
      if int(questiontones) == questiontones:
        questiontones = int(questiontones)

      # Question
      question = self.notedictionary.getNoteName(notenumber)+" "
      question += operationchar+" "
      question += str(questiontones)+" "
      if tonetype == 1:
        question += "semitone"
      else: #if tonetype == 2
        question += "tone"
      if questiontones > 1:
        question += "s"
      question += " = "

      # Player plays
      (answer, timetoanswer) = self.askQuestion(question)
      if answer == self.endGameString:
        continue

      # Actual answer
      correctnotenumber = self.notedictionary.getNotePlusSemitonesNumber(notenumber, noteshift)
      correctname = self.notedictionary.getNoteName(correctnotenumber)
      
      # Check if player got it right
      if self.notedictionary.doesStringMatchNoteNumber(Helpers.noAccentsOrSpaces(answer), correctnotenumber):
        self.handleAnswer(True, timetoanswer)
        print("Correct! "+str(self.score)+" in a row! It was indeed a "+correctname)
      else:
        self.handleAnswer(False, timetoanswer)
        print("WRONG! Actually it was a "+correctname)
    
    # After loop
    self.printBestScore()
