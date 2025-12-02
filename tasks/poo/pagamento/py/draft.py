from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor: float = valor
        self.descricao = descricao
    
    def resumo(self) -> str:
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    def validar_valor(self) -> None:
        if self.valor <= 0:
            raise ValueError("falhou: valor invalido")
    
    @abstractmethod
    def processar(self):
        pass
    
class CartaoCredito(Pagamento): #acoplamento forte
    def __init__(self, num: int, nome: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.num = num
        self.nome = nome
        self.limite: float = limite

    def resumo(self):
        return "Cartao de Credito: " + super().resumo()

    def get_limite(self):
        return self.limite

    def processar(self):
        if self.valor > self.limite:
            print("pagamento recusado por limite insuficiente")
            return
        self.limite -= self.valor

class Pix(Pagamento):
    def __init__(self, chave: str, banco: str, descricao: str, valor: float):
        super().__init__(valor, descricao)
        self.__chave = chave
        self.__banco = banco

    def resumo(self):
        return "Pix: " + super().resumo()

    def processar(self):
        if self.valor < 0:
            print("pagamento recusado pelo valor ser menor que 0")
            return
        print(f"{self.__banco} - {self.__chave}")

class Boleto(Pagamento):
    def __init__(self, codBar: str, vencimento: str, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.codBar = codBar
        self.vencimento = vencimento

    def resumo(self):
        return "Boleto: " + super().resumo()
    
    def processar(self):
        print(f"Boleto gerado. Aguardando pagamento...")

def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance(pag, CartaoCredito):
            print(pag.get_limite())

pag: Pagamento = CartaoCredito(nome= "David", descricao="Coxinha", limite=500.00, num=123, valor=0.50)
pag2: Pagamento = Pix(
    chave="chave-0-do-1-pix",
    banco="inter",
    descricao="salgado no china",
    valor=6.0
)
pag3: Pagamento = Boleto(
    codBar="12345678",
    vencimento="01/01/2026",
    valor=150.0,
    descricao="mensalidade da academia"
)
pagamentos: list[Pagamento] = [pag, pag2, pag3]
processar_pagamentos(pagamentos)