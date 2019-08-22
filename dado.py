
class Pessoa:
    def __init__(self,nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def dados(self):
        print (self.nome,idade,altura)

class Medico(Pessoa):

    def __init__(self,nome,idade,altura,crm):
        super().__init__(nome,idade,altura)
        self.crm = crm
    def crmm(self):
        print (self.crm)

class Paciente(Pessoa):

    def __init__(self,nome,idade,altura,sintomas):
        super().__init__(nome,idade,altura)
        self.sintomas = sintomas

    def sint(self):
        print (self.sintomas)

pessoa = Pessoa('Maria','25','1,70')
paciente = Paciente('George','30','1,80','dor de cabeça')
medico = Medico('Matheus','36','1,78','978566247')

print(Pessoa.dados)
print(Medico.crmm)
print(Paciente.sint)
