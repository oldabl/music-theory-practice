
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
    super().__init__()
    print("\nWelcome to chord number of scale game!")
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
    
    while answer != "q":
      keynumber = self.notedictionary.getRandomNoteNumber()

      # Pick a scale (difficulty handling)
      majororminor = 0
      if self.score > 15:
        majororminor = random.randint(0,1)

      # Select right scale
      if majororminor == 0:
        majorminorstring = "major"
        scale = MAJOR_SCALE
      else:
        majorminorstring = "minor"
        scale = MINOR_SCALE
      
      # Work out number of degrees we can do (difficulty handling)
      numberofchoicesromannumber = 2 + int(self.score/6)
      if numberofchoicesromannumber > len(scale):
        numberofchoicesromannumber = len(scale)
      romannumbernumber = random.randint(0, numberofchoicesromannumber-1)

      romannumberinfo = scale[romannumbernumber]
      keyinfo = self.notedictionary.getNotes()[keynumber]

      correctnotenumber = self.notedictionary.getNotePlusSemitonesNumber(keynumber, romannumberinfo[1])
      correctnotename = self.notedictionary.getNoteName(correctnotenumber, suffix=romannumberinfo[2])

      question = "What's chord "+romannumberinfo[0]+" of "+majorminorstring+" scale in key "+keyinfo[0]+"? "
      answer = input("\n"+question)
      if answer == "revision":
        self.printRevisions()
        continue
      
      if self.notedictionary.doesStringMatchNoteNumber(Helpers.noAccentsOrSpaces(answer), correctnotenumber, suffix=romannumberinfo[2], thresholdratio=0.95):
        self.handleScore(True)
        print("Correct! "+str(self.score)+" in a row! It was "+correctnotename+ " indeed")
      else:
        self.handleScore(False)
        print("WRONG! Actually it was "+correctnotename)
        print('Type "revisions" to revise scales')
    
    # After loop
    self.printBestScore()
