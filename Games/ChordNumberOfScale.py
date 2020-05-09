
import random
import Games.Helpers as Helpers

MAJOR_SCALE = {
#    (NUMBER,SEMITONES,TYPE)
  0: ('I'   ,0        ,""   ),
  1: ('II'  ,2        ,"m"  ),
  2: ('III' ,4        ,"m"  ),
  3: ('IV'  ,5        ,""   ),
  4: ('V'   ,7        ,""   ),
  5: ('VI'  ,9        ,"m"  ),
  6: ('VII' ,11       ,"dim"),
}
MINOR_SCALE = {
#    (NUMBER,SEMITONES,TYPE)
  0: ('I'   ,0,       "m"  ),
  1: ('II'  ,2        ,"dim"),
  2: ('III' ,3        ,""   ),
  3: ('IV'  ,5        ,"m"  ),
  4: ('V'   ,7        ,"m"  ),
  5: ('VI'  ,8        ,""   ),
  6: ('VII' ,10       ,""   ),
}

class ChordNumberOfScale(Helpers.Game):

  def __init__(self):
    print("\nWelcome to chord number of scale game!")
    super().__init__()
    self.setMaxDifficulty(360)
    self.printRevisions()
  
  def printRevisions(self):
    print("\nRevisions: chord(semitones to I)")
    for i in range(2):
      #Which scale
      scale = MAJOR_SCALE
      scalestring = "Major"
      if i == 1:
        scale = MINOR_SCALE
        scalestring = "Minor"
      #Assemble scale string
      scalestring += ":"
      for value in scale.values():
        scalestring += " "+value[0]+value[2] + "("+str(value[1])+")"
      print(scalestring)


  def play(self):
    answer = ""
    alwaysincludeminor = False
    
    self.printQuitInfo()
    while answer != self.endGameString:
      # Pick random key to start with
      if self.ratioMaxDifficulty(3):
        #Use sharps at high difficulty
        keynumber = self.notedictionary.getRandomNoteNumber()
      else:
        #Don't use sharps at low difficulty
        maxnotenumber = int(1 + self.difficulty/10)
        keynumber = self.notedictionary.getRandomNoteNumber(False, maxnotenumber)

      # Pick a scale
      if alwaysincludeminor:
        majororminor = random.randint(0,3) #More chance to get minor now we know major well
      else:
        majororminor = 0 #Always major
      if self.ratioMaxDifficulty(2):
        alwaysincludeminor = True

      # Select right scale according to pick
      if majororminor == 0:
        scale = MAJOR_SCALE
        minorchar=""
      else:
        scale = MINOR_SCALE
        minorchar="m"

      # Key name from scale and key number
      keyname = self.notedictionary.getNoteName(keynumber, suffix=minorchar)

      # Work out number of degrees we can do (difficulty handling)
      romannumbernumber = random.randint(1, 7) - 1
      romannumberinfo = scale[romannumbernumber]

      # Prepare answer
      correctnotenumber = self.notedictionary.getNotePlusSemitonesNumber(keynumber, romannumberinfo[1])
      correctnotename = self.notedictionary.getNoteName(correctnotenumber, suffix=romannumberinfo[2])

      # Prepare question
      question = "Chord "+romannumberinfo[0]+" of "+keyname+" scale? "
      (answer, timetoanswer) = self.askQuestion("\n"+question)
      if answer == "revisions":
        self.printRevisions()
        continue
      elif answer == self.endGameString:
        continue
      
      if self.notedictionary.doesStringMatchNoteNumber(Helpers.noAccentsOrSpaces(answer), correctnotenumber, suffix=romannumberinfo[2], thresholdratio=0.95):
        self.handleAnswer(True, timetoanswer)
        print("Correct! "+str(self.score)+" in a row! It was "+correctnotename+ " indeed")
      else:
        self.handleAnswer(False, timetoanswer)
        print("WRONG! Actually it was "+correctnotename)
        print('Type "revisions" to revise scales')
    
    # After loop
    self.printBestScore()
