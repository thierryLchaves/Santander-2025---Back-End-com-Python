class Pessoa:
    def __init__(self,nome,ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano = 2025
        return _ano - self._ano_nascimento
    

pessoa = Pessoa("Thierry",1996)
print(f"Nome : {pessoa.nome} \tIdade: {pessoa.idade}")


        