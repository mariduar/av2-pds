class cliente:
    def __init__(self, nome, anonascimento,sexo,limitedecredito, endereco):
        self.nome = nome
        self.anonascimento = anonascimento
        self.sexo= sexo
        self.limitedecredito = limitedecredito
        self.endereco= endereco
    
    def imprimir(self):
        print(self.nome)
        print(self.anodenascimento)
        print(self.sexo)
        print(self.limitedecredito)
        print(self.endereco)

cliente1 = cliente("maryana", "2007", "feminino", "500", "rua paranapanema 3221")
cliente1.imprimir()
