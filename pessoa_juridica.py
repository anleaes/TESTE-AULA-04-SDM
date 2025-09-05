from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self, nome, endereco, idade,  cnpj):
        super().__init__(nome,  endereco, idade)
        self._cnpj = cnpj

    def validar_cnpj(cnpj=None):
        if cnpj is not None:
            return True
        
        return False