from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, data_nascimento):
        super().__init__(nome,  endereco, idade)
        self._cpf = cpf
        self._data_nascimento = data_nascimento