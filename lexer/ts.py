from tag import Tag
from token import Token

class TS:

   def __init__(self):
      self.ts = {}


      self.ts['program'] = Token(Tag.KW_program, 'program')
      self.ts['begin'] = Token(Tag.KW_begin, 'begin')
      self.ts['end'] = Token(Tag.KW_end, 'end')
      self.ts['turn'] = Token(Tag.KW_turn, 'turn')
      self.ts['degrees'] = Token(Tag.KW_degrees, 'degrees')
      self.ts['forward'] = Token(Tag.KW_forward, 'forward')
      self.ts['repeat'] = Token(Tag.KW_repeat, 'repeat')
      self.ts['do'] = Token(Tag.KW_do, 'do')
      self.ts['print'] = Token(Tag.KW_print, 'print')
      self.ts['if'] = Token(Tag.KW_if, 'if')


   def getToken(self, lexema):
      token = self.ts.get(lexema)
      return token

   def addToken(self, lexema, token):
      self.ts[lexema] = token

   def printTS(self):
      for k, t in self.ts.items():
         print(k, ":", t.toString())
