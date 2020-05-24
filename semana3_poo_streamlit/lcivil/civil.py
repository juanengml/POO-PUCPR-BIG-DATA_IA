

class Volume(object):
  def __init__(self, base, altura, largura):
    self.base = base
    self.altura = altura 
    self.largura = largura
  def calcule(self):
    return self.base * self.altura * self.largura
