
from collections import OrderedDict
import unicodedata

constnotes = OrderedDict([
  ("C" , ("C" , "Do"  )),
  ("C#", ("C#", "Do#" , "Csharp", "Do dièse")),
  ("D" , ("D" , "Ré"  , "")),
  ("D#", ("D#", "Ré#" , "Dsharp", "Ré dièse")),
  ("E" , ("E" , "Mi"  )),
  ("F" , ("F" , "Fa"  )),
  ("F#", ("F#", "Fa#" , "Fsharp", "Fa dièse")),
  ("G" , ("G" , "Sol" )),
  ("G#", ("G#", "Sol#", "Gsharp", "Sol dièse")),
  ("A" , ("A" , "La"  )),
  ("A#", ("A#", "La#" , "Asharp", "La dièse")),
  ("B" , ("B" , "Si"  )),
])

#
# Provide a dictionary with all notes numbered from 0 to 11 (0:A 11:G#)
#
class NoteDictionary:
  notes = OrderedDict()

  def __init__(self):
    self.initialiseNotes()

  def getNotes(self):
    # for (key, value) in self.notes.items():
    #   print(key)
    #   print(value)
    return self.notes

  def initialiseNotes(self):
    i = 0
    for key in constnotes:
      self.notes[i] = [constnotes[key][0], constnotes[key][1]]
      tmplist = []
      for variant in constnotes[key]:
        tmplist.extend(self.getAllVariants(variant))
      tmplist = list(set(tmplist))
      self.notes[i].extend(tmplist)
      i += 1

  def getAllVariants(self, variant):
    resultlist = []
    resultlist.extend(self.getSpaceVariants(variant))
    resultlist.extend(self.getSpaceVariants(variant.lower()))
    resultlist.extend(self.getSpaceVariants(variant.upper()))
    return resultlist
  def getSpaceVariants(self, variant):
    resultlist = []
    resultlist.extend(self.getAccentsVariants(variant))
    resultlist.extend(self.getAccentsVariants(variant.replace(" ", "")))
    return resultlist
  def getAccentsVariants(self, variant):
    resultlist = [variant]
    variant = ''.join((c for c in unicodedata.normalize('NFD', variant) if unicodedata.category(c) != 'Mn'))
    resultlist.append(variant)
    return resultlist
