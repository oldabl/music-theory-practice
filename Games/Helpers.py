
from collections import OrderedDict
import unicodedata, random, os, sys, difflib, time
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
def cleanLinesAhead(numberoflines, keep=False):
  sys.stdout.write( (LINE_CLEAN+"\n") * numberoflines)
  if not keep:
    goBackUpLines(numberoflines)
  sys.stdout.flush()

def goBackUpLines(numberoflines):
  sys.stdout.write( UP_ONE_LINE * numberoflines)
  sys.stdout.flush()

def printThanks():
  print()
  print("🎉 Well played!")
  print("💖 Sponsor me at https://github.com/oldabl/music-theory-practice")



#
# Const ote dictionary
# Will add into it all variants
CONSTANT_NOTES = {
  0:  (["C"],                           ["Do"]),
  1:  (["C#", "Csharp", "Db", "Dflat"], ["Do#",  "Do dièse",  "Réb",  "Ré bémol"]),
  2:  (["D"],                           ["Ré"]),
  3:  (["D#", "Dsharp", "Eb", "Eflat"], ["Ré#",  "Ré dièse",  "Mib",  "Mi bémol"]),
  4:  (["E"],                           ["Mi"]),
  5:  (["F"],                           ["Fa"]),
  6:  (["F#", "Fsharp", "Gb", "Gflat"], ["Fa#",  "Fa dièse",  "Solb", "Sol bémol"]),
  7:  (["G"],                           ["Sol"]),
  8:  (["G#", "Gsharp", "Ab", "Aflat"], ["Sol#", "Sol dièse", "Lab",  "La bémol"]),
  9:  (["A"],                           ["La"]),
  10: (["A#", "Asharp", "Bb", "Bflat"], ["La#",  "La dièse",  "Sib",  "Si bémol"]),
  11: (["B"],                           ["Si"]),
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
        self.notes[key] = value[1]
      elif self.notetype == "alphabet":
        self.notes[key] = value[0]
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

  def isSharp(self, notenumber):
    return "#" in self.getNoteName(notenumber)

  def getNotes(self):
    return self.notes
  
  def getNotePlusSemitonesNumber(self, notenumber, numberofsemitones):
    return (notenumber+numberofsemitones)%len(self.notes)

  def getNoteVariants(self, notenumber):
    return self.notes[notenumber]

  def getNoteName(self, notenumber, suffix=""):
    return self.notes[notenumber][0]+suffix

  def getRandomNoteNumber(self, includesharp=True, maxnotenumber=12):
    randomnotenumber = random.randint(0, min(len(self.notes), maxnotenumber)-1)
    if not includesharp and "#" in self.getNoteName(randomnotenumber):
      return randomnotenumber-1
    else:
      return randomnotenumber

  def doesStringMatchNoteNumber(self, trystring, notenumber, suffix="", thresholdratio=0.86):
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
      value = value+suffix
      for trys in trystrings:
        ratio = difflib.SequenceMatcher(None, trys, value).quick_ratio()
        if ratio > bestratio:
          bestratio = ratio

    # Look at ratio
    if bestratio >= thresholdratio:
      return True
    return False # else




#
# Any game will need a note dictionary and score handling
#
class Game:

  def __init__(self):
    clearTerminal()
    self.notedictionary = NoteDictionary()
    self.endGameString = "quit"
    self.bestscore = 0
    self.score = 0
    self.difficulty = 0
    self.maxdifficulty = None
    self.missedinarow = 0
    self.gotinarow = 0

  def printQuitInfo(self):
    print("To quit, type '"+self.endGameString+"'\n")

  def handleAnswer(self, correctanswer, timetoanswer = 0):
    if correctanswer and timetoanswer > 10:
      #10+ seconds to answer right, no increase in difficulty and row
      pass
    else:
      self.handleInARow(correctanswer)
      self.handleDifficulty(correctanswer)
    self.handleScore(correctanswer)
  
  def handleInARow(self, correctanswer):
    if correctanswer:
      self.gotinarow += 1
      self.missedinarow = 0
    else:
      self.gotinarow = 0
      self.missedinarow += 1

  def handleScore(self, correctanswer):
    if correctanswer:
      self.score += 1
    else:
      self.score = 0
    # Update best score
    if self.score > self.bestscore:
      self.bestscore = self.score

  def handleDifficulty(self, correctanswer):
    if correctanswer:
      byhowmuch = min(1+self.gotinarow*0.025, 1.2)
      self.difficulty += 1
      self.difficulty *= byhowmuch
    else:
      byhowmuch = max(1-self.missedinarow*0.05, 0.1)
      self.difficulty *= byhowmuch
    # Make sure we don't go over or under
    if self.maxdifficulty:
      self.difficulty = min(self.difficulty, self.maxdifficulty)
    self.difficulty = max(self.difficulty, 0)
    print(int(self.difficulty), end='')

  def reachedMaxDifficulty(self):
    self.maxdifficulty = self.difficulty

  def setMaxDifficulty(self, max):
    self.maxdifficulty = max

  def ratioMaxDifficulty(self, ratio):
    return self.difficulty >= self.maxdifficulty/ratio
  
  def askQuestion(self, question):
    start = time.time()
    answer = input(question)
    return (answer, time.time()-start)

  def printBestScore(self):
    print("Your best score on this session was: "+str(self.bestscore))
