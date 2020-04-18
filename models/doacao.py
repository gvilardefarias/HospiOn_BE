class doacao():
    ID           = -1

    destinatario = Hospital()
    doador       = Doador()
    produto      = Produto()
    confirmada   = False

    def __init__(self, doador, destinatario, produto):
        self.destinatario = destinatario
        self.doador       = doador
        self.produto      = produto

