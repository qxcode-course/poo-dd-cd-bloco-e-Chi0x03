from abc import ABC, abstractmethod

class Veiculo(ABC):
  def __init__(self, id: str, entrada, tipo: str):
    self.__id: str = id
    self.__entrada = entrada
    self.__tipo: str = tipo

  def setEntrada(self, entrada: int):
    self.__entrada = entrada

  def getEntrada(self) -> int:
    return self.__entrada
  
  def getTipo(self) -> str:
    return self.__tipo
  
  def getId(self) -> str:
    return self.__id

  @abstractmethod
  def calcularValor(self, horaSaida: int) -> float:
    pass

  def __str__(self):
    return f"{self.__tipo:_>10} : {self.__id:_>10} : {self.__entrada:_>2}"

class Bike(Veiculo):
  def __init__(self, id: str):
    super().__init__(id, 0, "Bike")

  def calcularValor(self, horaSaida: int):
    return 3
  
class Moto(Veiculo):
  def __init__(self, id: str):
    super().__init__(id, 0, "Moto")

  def calcularValor(self, horaSaida: int):
    horasEstacionado = horaSaida - self.getEntrada()
    return horasEstacionado // 20
  
class Carro(Veiculo):
  def __init__(self, id: str):
    super().__init__(id, 0, "Carro")

  def calcularValor(self, horaSaida: int):
    horasEstacionado = horaSaida - self.getEntrada()
    valorASerPago = horasEstacionado // 10
    if valorASerPago < 5:
      return 5
    return valorASerPago
  
class Estacionamento:
  def __init__(self):
    self.__veiculos: list[Veiculo] = []
    self.__horaAtual = 0

  def procurarVeiculo(self, id: str) -> Veiculo | None:
    for veiculo in self.__veiculos:
      if veiculo.getId() == id:
        return veiculo
    return None
  
  def estacionar(self, veiculo: Veiculo):
    if self.procurarVeiculo(veiculo.getId()) is not None:
      raise Exception("Veículo já está estacionado.")
    self.__veiculos.append(veiculo)

  def pagar(self, id: str):
    veiculo = self.procurarVeiculo(id)
    if veiculo is None:
      raise Exception("Veículo não está estacionado.")
    valor = veiculo.calcularValor(self.getHoraAtual())
    print(f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} saiu {self.getHoraAtual()}. Pagar R$ {valor:.2f}")

  def passarTempo(self, horas: int):
    self.__horaAtual += horas

  def getHoraAtual(self) -> int:
    return self.__horaAtual
  
    
  def __str__(self):
    veiculosStr = "\n".join([str(v) for v in self.__veiculos])
    if len(self.__veiculos) != 0:
      veiculosStr += "\n"
    return f"{veiculosStr}Hora atual: {self.__horaAtual}"
  

def criarVeiculo(tipo: str, id: str) -> Veiculo:
  if tipo.upper() == "BIKE":
    return Bike(id)
  elif tipo.upper() == "MOTO":
    return Moto(id)
  elif tipo.upper() == "CARRO":
    return Carro(id)
  else:
    raise Exception("Tipo de veículo inválido.")

def main():
  estacionamento = Estacionamento()
  while True:
    cmd = input()
    args = cmd.split()

    print("$"+cmd)

    if args[0] == "show":
      print(estacionamento)
    elif args[0] == "tempo":
      horas = int(args[1])
      estacionamento.passarTempo(horas)
    elif args[0] == "estacionar":
      tipo = args[1]
      id = args[2]
      veiculo = criarVeiculo(tipo, id)
      veiculo.setEntrada(estacionamento.getHoraAtual())
      estacionamento.estacionar(veiculo)
    elif args[0] == "pagar":
      id = args[1]
      estacionamento.pagar(id)
    elif args[0] == "end":
      break
    else:
      print("Comando inválido.")

if __name__ == "__main__":
  try:
    main()
  except Exception as e:
    print(f"Erro: {e}")