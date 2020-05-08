
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

  def play(self):
    answer = ""
    
    while answer != "q":
      keynumber = self.notedictionary.getRandomNoteNumber()

      numberofchoicesromannumber = 2 + int(self.score/6)
      if numberofchoicesromannumber > len(MAJOR_SCALE):
        numberofchoicesromannumber = len(MAJOR_SCALE)
      romannumbernumber = random.randint(0, numberofchoicesromannumber-1)

      romannumberinfo = MAJOR_SCALE[romannumbernumber]
      keyinfo = self.notedictionary.getNotes()[keynumber]

      correctnotenumber = self.notedictionary.getNotePlusSemitonesNumber(keynumber, romannumberinfo[1])
      correctnotename = self.notedictionary.getNoteName(correctnotenumber)

      question = "What's chord "+romannumberinfo[0]+" of major scale in key "+keyinfo[0]+"? "
      answer = input("\n"+question)
      
      if answer in self.notedictionary.getNoteVariants(correctnotenumber):
        self.handleScore(True)
        print("Correct! "+str(self.score)+" in a row! It was "+correctnotename+ " indeed")
      else:
        self.handleScore(False)
        print("WRONG! Actually it was "+correctnotename)
    
    # After loop
    self.printBestScore()
