
from collections import OrderedDict
import unicodedata, random, os, sys, difflib
from os import name, system



def clearTerminal(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



def noAccentsOrSpaces(string):
  string = string.lower()
  string = string.replace(" ", "")
  string = ''.join((c for c in unicodedata.normalize('NFD', string) if unicodedata.category(c) != 'Mn'))
  return string



LINE_CLEAN = " "*os.get_terminal_size()[0]+"\r"
UP_ONE_LINE = "\033[F"
def cleanLinesAhead(numberoflines):
  sys.stdout.write( (LINE_CLEAN+"\n") * numberoflines)
  sys.stdout.write( UP_ONE_LINE * numberoflines)

def goBackUpLines(numberoflines):
  sys.stdout.write( UP_ONE_LINE * numberoflines)

def printThanks():
  print()
  print("🎉 Well played!")
  print("💖 Sponsor me at https://github.com/oldabl/music-theory-practice")



#
# Const ote dictionary
# Will add into it all variants
CONSTANT_NOTES = {
  0:  (["C"],           ["Do"]),
  1:  (["C#", "Csharp"],["Do#", "Do dièse"]),
  2:  (["D"],           ["Ré"]),
  3:  (["D#", "Dsharp"],["Ré#", "Ré dièse"]),
  4:  (["E"],           ["Mi"]),
  5:  (["F"],           ["Fa"]),
  6:  (["F#", "Fsharp"],["Fa#", "Fa dièse"]),
  7:  (["G"],           ["Sol"]),
  8:  (["G#", "Gsharp"],["Sol#", "Sol dièse"]),
  9:  (["A"],           ["La"]),
  10: (["A#", "Asharp"],["La#", "La dièse"]),
  11: (["B"],           ["Si"]),
}
HOW_MANY_NOTES = len(CONSTANT_NOTES)

#
# Provide a dictionary with all notes numbered from 0 to 11 (0:A 11:G#)
#
class NoteDictionary:

  def __init__(self):
    self.notetype = "traditional"
    if "MOZARTWILLIAMS" in os.environ:
      self.notetype = os.environ["MOZARTWILLIAMS"]
    self.notes = dict()
    self.initialiseDictionary()

  def initialiseDictionary(self):
    for (key, value) in CONSTANT_NOTES.items():
      if self.notetype == "traditional":
        self.notes[key] = value[1] + value[0]
      elif self.notetype == "alphabet":
        self.notes[key] = value[0] + value[1]
    self.formatVariants()

  def formatVariants(self):
    for key in self.notes:
      tmplist = []
      for variant in self.notes[key]:
        tmplist.append(noAccentsOrSpaces(variant))
      tmplist = list(set(tmplist))
      self.notes[key].extend(tmplist)
    # for (key, value) in self.notes.items():
    #   print(key)
    #   print(value)

  def getNotes(self):
    return self.notes
  
  def getNotePlusSemitonesNumber(self, notenumber, numberofsemitones):
    return (notenumber+numberofsemitones)%len(self.notes)

  def getNoteVariants(self, notenumber):
    return self.notes[notenumber]

  def getNoteName(self, notenumber):
    return self.notes[notenumber][0]

  def getRandomNoteNumber(self, includesharp=True):
    randomnotenumber = random.randint(0, len(self.notes)-1)
    if not includesharp and "#" in self.getNoteName(randomnotenumber):
      return self.getRandomNoteNumber(includesharp)
    else:
      return randomnotenumber

  def doesStringMatchNoteNumber(self, trystring, notenumber):
    bestratio = 0.0
    # Will try replacing the diese or sharp with #
    trystring1 = trystring
    trystring1 = trystring1.replace("diese", "#")
    trystring1 = trystring1.replace("sharp", "#")
    # Will try replacing the # with sharp or diese
    trystring2 = trystring
    if self.notetype == "alphabet":
      trystring2 = trystring2.replace("#", "sharp")
    elif self.notetype == "traditional":
      trystring2 = trystring2.replace("#", "diese")
    # List of strings to try
    trystrings = [trystring, trystring1, trystring2]
    trystrings = list(set(trystrings))
    # Check every try string on every variant
    for value in self.getNoteVariants(notenumber):
      for trystring in trystrings:
        ratio = difflib.SequenceMatcher(None, trystring, value).ratio()
        if ratio > bestratio:
          bestratio = ratio

    # Look at ratio
    if bestratio > 0.8:
      return True
    return False # else




#
# Any game will need a note dictionary and score handling
#
class Game:

  def __init__(self):
    clearTerminal()
    self.notedictionary = NoteDictionary()
    self.score = 0
    self.bestscore = 0

  def handleScore(self, correctanswer):
    if correctanswer:
      self.score += 1
    else:
      self.score = 0
    # Update best score
    if self.score > self.bestscore:
      self.bestscore = self.score

  def printBestScore(self):
    print("Your best score on this session was: "+str(self.bestscore))
