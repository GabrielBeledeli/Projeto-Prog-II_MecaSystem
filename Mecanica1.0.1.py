# SISTEMA DE GERENCIAMENTO DE OFICINA MECANICA
def cabecalho(strg):
    print(f'-'*60)
    print(f'{strg :^60}')
    print(f'-'*60)

cabecalho('SISTEMA DE GERENCIAMNETO DE OFICINA MECÂNICA')

class geral():
    def __init__ (self, nome, cpf, cidade, estado, rua, bairro, numero, c_modelo, c_marca, c_ano, c_cor):
        self.nome = nome
        self.cpf = cpf
        self.cidade = cidade
        self.estado = estado
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.c_modelo = c_modelo
        self.c_marca = c_marca
        self.c_ano = c_ano
        self.c_cor = c_cor
        
    def print_cadastro_pessoa(self):
        cabecalho('INFO CADASTRO PESSOA')
        print(self.nome, '\n',self.cpf,'\n',self.cidade,'\n',self.estado,'\n',self.rua,'\n',self.bairro,'\n',self.numero)
        
    def print_cadastro_carro(self):
        cabecalho('INFO CADASTRO CARRO')
        print(self.c_modelo,'\n',self.c_marca,'\n',self.c_ano,'\n',self.c_cor)

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
            
tudo = geral(nome, cpf, cidade, estado, rua, bairro, numero, c_modelo, c_marca, c_ano, c_cor)
tudo.print_cadastro_pessoa()
tudo.print_cadastro_carro()
