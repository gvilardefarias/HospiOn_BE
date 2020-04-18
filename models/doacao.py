class doacao():
    ID           = -1

    destinatario = Hospital()
    doador       = Doador()
    produto      = ""
    confirmada   = False

    def __init__(self, doador, destinatario, produto):
        self.destinatario = destinatario
        self.doador       = doador
        self.produto      = produto

    def realizarDoacao(self, doador):
        self.doador = doador
