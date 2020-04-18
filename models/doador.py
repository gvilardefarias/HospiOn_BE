class doador():
    nome     = ""
    tipo     = "" # PJ ou PF
    
    email    = ""
    senha    = ""

    def __init__(self, nome, tipo, email, senha):
        self.nome  = nome
        self.tipo  = tipo
        self.email = email
        self.senha = senha

    def fazerDoacao(doacao):
        self.doacoes.append(doacao)

class doadorPF(doador):
    idade = -1
    cpf   = ""

    def __init__(self, nome, tipo, email, senha, idade, cpf):
        super().__init__(nome, "PF", email, senha)

        self.idade = idade
        self.cpf   = cpf

class doadorPJ(doador):
    cnpj = ""

    def __init__(self, nome, tipo, email, senha, cnpj):
        super().__init__(nome, "PJ", email, senha)

        self.cnpj = cnpj
