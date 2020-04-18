class DadosBancarios():
    conta   = ""
    agencia = ""
    banco   = ""

class Endereco():
    latitude  = False
    longitude = False

    def __init__(self, latitude, longitude):
        self.latitude  = latitude
        self.longitude = longitude

class Hospital():
    nome           = ""
    endereco       = Endereco()
    dadosBancarios = DadosBancarios()
    
    def __init__(self, nome, endereco, dadosBancarios):
        self.nome           = nome
        self.endereco       = endereco
        self.dadosBancarios = dadosBancarios
        

