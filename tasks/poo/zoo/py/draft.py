from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self, nome: str):
    self.nome = nome

  def apresentar_nome(self):
    print(f"Eu sou um(a) {self.nome}!")

  @abstractmethod
  def fazer_som(self):
    pass

  @abstractmethod
  def mover(self):
    pass


class Leao(Animal):
  def __init__(self, nome:str):
    super().__init__(nome)

  def fazer_som(self):
    print("Raaarrr!")

  def mover(self):
    print("Se movendo para ir dormir")


class Elefante(Animal):
  def __init__(self, nome:str):
    super().__init__(nome)

  def fazer_som(self):
    print("Prrrrrr!")

  def mover(self):
    print("Caminhando lentamente")

class Galinha(Animal):
  def __init__(self, nome:str):
    super().__init__(nome)

  def fazer_som(self):
    print("Có có có!")

  def mover(self):
    print("Bicando pelo chão")

class Estudante(Animal):
  def __init__(self, nome:str):
    super().__init__(nome)

  def fazer_som(self):
    print("Estudando...")

  def mover(self):
    print("Indo para a aula")

def apresentar(animal: Animal):
  animal.apresentar_nome()
  animal.fazer_som()
  animal.mover()
  print(type(animal).__name__)

lista: list[Animal] = [
  Leao("Leão preguiçososão"),
  Elefante("Elefante caminhão"),
  Galinha("Galinha pintadinha"),
  Estudante("Estudante que estuda")
]

for animal in lista:
  apresentar(animal)