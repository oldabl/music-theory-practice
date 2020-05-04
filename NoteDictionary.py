
from collections import OrderedDict

constnotes = OrderedDict([ 
  ("A" , ("A" , "La"  )),
  ("A#", ("A#", "La#" )),
  ("B" , ("B" , "Si"  )),
  ("C" , ("C" , "Do"  )),
  ("C#", ("C#", "Do#" )),
  ("D" , ("D" , "Ré"  )),
  ("D#", ("D#", "Ré#" )),
  ("E" , ("E" , "Mi"  )),
  ("F" , ("F" , "Fa"  )),
  ("F#", ("F#", "Fa#" )),
  ("G" , ("G" , "Sol" )),
  ("G#", ("G#", "Sol#")),
])

#
# Provide a dictionary with all notes numbered from 0 to 11 (0:A 11:G#)
#
class NoteDictionary:
  notes = OrderedDict()

  def __init__(self):
    self.initialiseNotes()

  def initialiseNotes(self):
    i = 0
    for key in constnotes:
      self.notes[i] = [constnotes[key][0], constnotes[key][1]]
      for variant in constnotes[key]:
        self.notes[i].append(variant.lower())
        self.notes[i].append(variant.upper())
      i += 1

  def getNotes(self):
    return self.notes
