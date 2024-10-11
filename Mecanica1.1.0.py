# SISTEMA DE GERENCIAMENTO DE OFICINA MECANICA
import os
# Função para print de mensagens no terminal
def cabecalho(strg):
    print(f'-'*60)
    print(f'{strg :^60}')
    print(f'-'*60)

# lista de cores
cores = ['\033[m',           # 0 sem cor
         '\033[0;31m',    # 1 vermelho
         '\033[0;32m',    # 2 verde   
         '\033[0;30;43m',    # 3 amarelo
         '\033[0;30;44m',    # 4 azul
         '\033[0;30;45m',    # 5 roxo
         '\033[40m']         # 6 branco

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
        
# Cadastro Pessoa
cabecalho('CADASTRO PESSOA')
# Laço de verificação das informações recebidas pelo usuário
while True:
    try:
        nome = input('NOME: ').strip()  # remove espaços extras no início e no fim
        if not nome:  # Verifica se o nome é uma string vazia após remover espaços
            raise ValueError('O Nome não pode ser vazio ou conter apenas espaços!')
        if not all(x.isalpha() or x.isspace() for x in nome): # Verifica se o caractere x é uma letra ou um espaço. Se for uma dessas duas opções, retorna True. Caso contrário, retorna False.
            raise ValueError('O Nome deve conter apenas letras e espaços!')
    except ValueError as e: # Retorna e informa o ERRO
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break  # interrompe o laço

while True:
    try:
        cpf = input('CPF (somente números, sem espaços ou pontos): ').strip()  # Mantém como string e remove espaços em volta
        if not cpf:
            raise ValueError('O CPF não pode ser vazio!')
        if not cpf.isdigit():  # Verifica se todos os caracteres são dígitos
            raise ValueError('O CPF deve conter apenas números!')
        if len(cpf) != 11:  # CPF deve ter 11 dígitos
            raise ValueError('O CPF deve ter 11 dígitos!')
    except ValueError as e:
        print(f'{cores[1]}ERRO: {e}{cores[0]}')
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break  # interrompe o laço

while True:
    try:
        cidade = str(input('CIDADE: ')).strip()     
        if not cidade:     
            raise ValueError('o nome da Cidade não pode ser vazio ou conter apenas espaços!')
        if not all(x.isalpha() or x.isspace() for x in cidade):    
            raise ValueError('O nome da Cidade deve conter apenas letras e espaços!')
    except ValueError as e:   
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

while True:
    try:
        estado = str(input('ESTADO: ')).strip()     
        if not estado:     
            raise ValueError('o nome do Estado não pode ser vazio ou conter apenas espaços!')
        if not all(x.isalpha() or x.isspace() for x in estado):    
            raise ValueError('O nome do Estado deve conter apenas letras e espaços!')
    except ValueError as e:   
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

while True:
    try:
        rua = str(input('RUA: ')).strip()     
        if not rua:     
            raise ValueError('o nome da Rua não pode ser vazio ou conter apenas espaços!')
        if not all(x.isalpha() or x.isspace() for x in rua):    
            raise ValueError('O nome da Rua deve conter apenas letras e espaços!')
    except ValueError as e:   
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

while True:
    try:
        bairro = str(input('BAIRRO: ')).strip()     
        if not bairro:     
            raise ValueError('o nome do Bairro não pode ser vazio ou conter apenas espaços!')
        if not all(x.isalpha() or x.isspace() for x in bairro):    
            raise ValueError('O nome do Bairro deve conter apenas letras e espaços!')
    except ValueError as e:   
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

while True:
    try:
        numero = str(input('NUMERO: ')).strip()     
        if not numero:
            raise ValueError('O Número não pode ser vazio!')
        if not numero.isdigit():     
            raise ValueError('O Número deve conter apenas digitos numéricos!')
    except ValueError as e:
        print(f'{cores[1]}ERRO: {e}{cores[0]}')
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

# Cadastro carro
cabecalho('CADASTRO CARRO')
while True:
    try:
        c_modelo = str(input('MODELO: ')).strip()     
        if not c_modelo:     
            raise ValueError('o Modelo do carro não pode ser vazio ou conter apenas espaços!')
    except ValueError as e:   
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

while True:
    try:
        c_marca = str(input('MARCA: ')).strip()     
        if not c_marca:     
            raise ValueError('A Marca do carro não pode ser vazio ou conter apenas espaços!')
        if not all(x.isalpha() or x.isspace() for x in c_marca):    
            raise ValueError('A Marca do carro deve conter apenas letras e espaços!')
    except ValueError as e:   
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

while True:
    try:
        c_ano = str(input('ANO: ')).strip()     
        if not c_ano:
            raise ValueError('O Ano não pode ser vazio!')
        if not c_ano.isdigit():     
            raise ValueError('O Ano deve conter apenas números!')
        if len(c_ano) != 4:  # Ano deve ter 4 dígitos
            raise ValueError('O Ano deve ter 4 dígitos!')
    except ValueError as e:
        print(f'{cores[1]}ERRO: {e}{cores[0]}')
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

while True:
    try:
        c_cor = str(input('COR: ')).strip()     
        if not c_cor:     
            raise ValueError('A Marca do carro não pode ser vazio ou conter apenas espaços!')
        if not all(x.isalpha() or x.isspace() for x in c_cor):    
            raise ValueError('A Marca do carro deve conter apenas letras e espaços!')
    except ValueError as e:   
        print(f'{cores[1]}ERRO: {e}{cores[0]}') 
    else:
        print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
        break   

# limpar terminal
os.system('cls')

# Chamada da SubClasse
tudo = carro(nome, cpf, cidade, estado, rua, bairro, numero, c_modelo, c_marca, c_ano, c_cor)
tudo.print_cadastro_carro()