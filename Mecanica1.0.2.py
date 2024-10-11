# SISTEMA DE GERENCIAMENTO DE OFICINA MECANICA
def cabecalho(strg):
    print(f'-'*60)
    print(f'{strg :^60}')
    print(f'-'*60)

cabecalho('SISTEMA DE GERENCIAMENTO DE OFICINA MECÂNICA')

# SuperClasse (dados genéricos de cadastro: nome, cpf, cidade, estado, rua, bairro, numero)
class pessoal():
    def __init__ (self, nome, cpf, cidade, estado, rua, bairro, numero):
        self.nome = nome
        self.cpf = cpf
        self.cidade = cidade
        self.estado = estado
        self.rua = rua
        self.bairro = bairro
        self.numero = numero        
    def sobre_cadastro_pessoa(self):   
        return (f'NOME: {self.nome}\nCPF: {self.cpf}\nCIDADE: {self.cidade}\nESTADO: {self.estado}\nRUA: {self.rua}\nBAIRRO: {self.bairro}\nNUMERO: {self.numero}')

# SubClasse (dados específicos: c_modelo, c_marca, c_ano, c_cor)
class carro(pessoal):
    def __init__(self, nome, cpf, cidade, estado, rua, bairro, numero, c_modelo, c_marca, c_ano, c_cor):
        super().__init__(nome, cpf, cidade, estado, rua, bairro, numero)
        self.c_modelo = c_modelo
        self.c_marca = c_marca
        self.c_ano = c_ano
        self.c_cor = c_cor
    def print_cadastro_carro(self):
        cabecalho('DADOS PESSOAIS')
        print(f'{super().sobre_cadastro_pessoa()}')
        cabecalho('DADOS VEICULO')
        print(f'MODELO: {self.c_modelo}\nMARCA: {self.c_marca}\nANO: {self.c_ano}\nCOR: {self.c_cor}')
    def sobre_cadastro_carro(self):
        return (f'MODELO: {self.c_modelo}\nMARCA: {self.c_marca}\nANO: {self.c_ano}\nCOR: {self.c_cor}')
        

cabecalho('CADASTRO PESSOA')

nome = str(input('NOME: '))
cpf = int(input('CPF: '))
cidade = str(input('CIDADE: '))
estado = str(input('ESTADO: '))
rua = str(input('RUA: '))
bairro = str(input('BAIRRO: '))
numero = int(input('NUMERO: '))
cabecalho('CADASTRO CARRO')
c_modelo = str(input('MODELO: '))
c_marca = str(input('MARCA: '))
c_ano = int(input('ANO: '))
c_cor = str(input('COR: '))
            
tudo = carro(nome, cpf, cidade, estado, rua, bairro, numero, c_modelo, c_marca, c_ano, c_cor)
tudo.print_cadastro_carro()
