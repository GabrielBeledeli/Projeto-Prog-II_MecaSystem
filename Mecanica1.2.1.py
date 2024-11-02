# SISTEMA DE GERENCIAMENTO DE OFICINA MECANICA
import os
import pandas as pd
import csv

# Função para print de mensagens no terminal


def cabecalho(strg):
    print(f'-'*60)
    print(f'{strg:^60}')
    print(f'-'*60)

# Funcao para pausar


def pausar():
    os.system('pause')

# Funcao para limpar


def limpar():
    os.system('cls')


# lista de cores
cores = ['\033[m',           # 0 sem cor
         '\033[0;31m',       # 1 vermelho
         '\033[0;32m',       # 2 verde
         '\033[0;30;43m',    # 3 amarelo
         '\033[0;30;44m',    # 4 azul
         '\033[0;30;45m',    # 5 roxo
         '\033[40m']         # 6 branco

cabecalho('SISTEMA DE GERENCIAMENTO DE OFICINA MECÂNICA')

# SuperClasse (dados genéricos de cadastro: nome, cpf, cidade, estado, rua, bairro, numero)


class pessoal():
    def __init__(self, nome, cpf, cidade, estado, rua, bairro, numero):
        self.nome = nome
        self.cpf = cpf
        self.cidade = cidade
        self.estado = estado
        self.rua = rua
        self.bairro = bairro
        self.numero = numero

    def sobre_cadastro_pessoa(self):
        return (f'NOME: {self.nome}\nCPF: {self.cpf}\nCIDADE: {self.cidade}\nESTADO: {self.estado}\nRUA: {self.rua}\nBAIRRO: {self.bairro}\nNUMERO: {self.numero}')

# SubClasse (dados específicos: v_modelo, v_marca, v_ano, v_cor)


class veiculo(pessoal):
    def __init__(self, nome, cpf, cidade, estado, rua, bairro, numero, v_modelo, v_marca, v_ano, v_cor):
        super().__init__(nome, cpf, cidade, estado, rua, bairro, numero)
        self.v_modelo = v_modelo
        self.v_marca = v_marca
        self.v_ano = v_ano
        self.v_cor = v_cor

    def sobre_cadastro_veiculo(self):
        return (f'MODELO: {self.v_modelo}\nMARCA: {self.v_marca}\nANO: {self.v_ano}\nCOR: {self.v_cor}')

# Subclasse Serviço


class servicos(veiculo):
    def __init__(self, nome, cpf, cidade, estado, rua, bairro, numero, v_modelo, v_marca, v_ano, v_cor, servico, orcamento):
        super().__init__(nome, cpf, cidade, estado, rua,
                         bairro, numero, v_modelo, v_marca, v_ano, v_cor)
        self.servico = servico
        self.orcamento = orcamento

    def sobre_servicos(self):
        return (f'SERVIÇO: {self.servico}\nORÇAMENTO: {self.orcamento}')


class pecas(servicos):
    def __init__(self, nome, cpf, cidade, estado, rua, bairro, numero, v_modelo, v_marca, v_ano, v_cor, servico, orcamento, peca, quantidade, valor):
        super().__init__(nome, cpf, cidade, estado, rua, bairro, numero,
                         v_modelo, v_marca, v_ano, v_cor, servico, orcamento)
        self.peca = peca
        self.quantidade = quantidade
        self.valor = valor

    def print_pecas(self):
        cabecalho('DADOS PESSOAIS')
        print(f'{super().sobre_cadastro_pessoa()}')
        cabecalho('DADOS VEICULO')
        print(f'{super().sobre_cadastro_veiculo()}')
        cabecalho('SERVIÇOS')
        print(f'{super().sobre_servicos()}')
        cabecalho('PECAS')
        print(f'PECAS: {self.peca}\nQUANTIDADE: {
              self.quantidade}\nVALOR: {self.valor}')

    def sobre_pecas(self):
        return (f'PECAS: {self.peca}\nQUANTIDADE: {self.quantidade}\nVALOR: {self.valor}')
    # quero que aqui seja uma funcao que crie arquivo csv com o nome herdado da classe principal cadastropessoas

    def exportar_para_csv(self):
        # Define o nome do arquivo baseado no nome do cliente
        nome_arquivo = f"{self.nome.replace(' ', '_')}_servico.csv"
        # Define os dados para exportação
        dados = [
            ['Nome', 'CPF', 'Cidade', 'Estado', 'Rua', 'Bairro', 'Numero', 'Modelo Veiculo',
                'Marca', 'Ano', 'Cor', 'Servico', 'Orcamento', 'Peca', 'Quantidade', 'Valor'],
            [self.nome, self.cpf, self.cidade, self.estado, self.rua, self.bairro, self.numero, self.v_modelo,
                self.v_marca, self.v_ano, self.v_cor, self.servico, self.orcamento, self.peca, self.quantidade, self.valor]
        ]

        # Cria o arquivo CSV e escreve os dados
        with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerows(dados)
        print(f"Dados exportados com sucesso para {nome_arquivo}")

# Função para revisar serviço


def revisar_servico():
    cliente_nome = str(input(
        "Digite o nome do cliente para revisar o serviço: ")).strip().replace(" ", "_")
    arquivo_csv = f"{cliente_nome}_servico.csv"
    if os.path.exists(arquivo_csv):
        df = pd.read_csv(arquivo_csv)

        cabecalho('DADOS PESSOAIS')
        print(f'NOME: {df["Nome"][0]}')
        print(f'CPF: {df["CPF"][0]}')
        print(f'CIDADE: {df["Cidade"][0]}')
        print(f'ESTADO: {df["Estado"][0]}')
        print(f'RUA: {df["Rua"][0]}')
        print(f'BAIRRO: {df["Bairro"][0]}')
        print(f'NUMERO: {df["Numero"][0]}')

        cabecalho('DADOS VEICULO')
        print(f'MODELO: {df["Modelo Veiculo"][0]}')
        print(f'MARCA: {df["Marca"][0]}')
        print(f'ANO: {df["Ano"][0]}')
        print(f'COR: {df["Cor"][0]}')

        cabecalho('SERVIÇOS')
        print(f'SERVIÇO: {df["Servico"][0]}')
        print(f'ORÇAMENTO: {df["Orcamento"][0]}')

        cabecalho('PEÇAS')
        print(f'PEÇA: {df["Peca"][0]}')
        print(f'QUANTIDADE: {df["Quantidade"][0]}')
        print(f'VALOR: {df["Valor"][0]}')
    else:
        print(f"{cores[1]}Erro: Arquivo para o cliente '{
              cliente_nome}' não encontrado!{cores[0]}")


# Menu inicial
while True:
    limpar()
    cabecalho("MENU INICIAL")
    print("Escolha uma opção:")
    print("1 - Cadastrar novo cliente")
    print("2 - Revisar serviço de cliente cadastrado")
    print("3 - Sair")
    opcao = input("Digite sua escolha (1,2 ou 3): ").strip()

    if opcao == '1':
        limpar()
        # Cadastro Pessoa
        cabecalho('CADASTRO PESSOA')
        # Laço de verificação das informações recebidas pelo usuário
        while True:
            try:
                # remove espaços extras no início e no fim
                nome = str(input('NOME: ')).strip()
                if not nome:  # Verifica se o nome é uma string vazia após remover espaços
                    raise ValueError(
                        'O Nome não pode ser vazio ou conter apenas espaços!')
                # Verifica se o caractere x é uma letra ou um espaço. Se for uma dessas duas opções, retorna True. Caso contrário, retorna False.
                if not all(x.isalpha() or x.isspace() for x in nome):
                    raise ValueError(
                        'O Nome deve conter apenas letras e espaços!')
            except ValueError as e:  # Retorna e informa o ERRO
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break  # interrompe o laço

        while True:
            try:
                # Mantém como string e remove espaços em volta
                cpf = str(input(
                    'CPF (somente números, sem espaços ou pontos): ')).strip()
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
                    raise ValueError(
                        'o nome da Cidade não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in cidade):
                    raise ValueError(
                        'O nome da Cidade deve conter apenas letras e espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                estado = str(input('ESTADO: ')).strip()
                if not estado:
                    raise ValueError(
                        'o nome do Estado não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in estado):
                    raise ValueError(
                        'O nome do Estado deve conter apenas letras e espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                rua = str(input('RUA: ')).strip()
                if not rua:
                    raise ValueError(
                        'o nome da Rua não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in rua):
                    raise ValueError(
                        'O nome da Rua deve conter apenas letras e espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                bairro = str(input('BAIRRO: ')).strip()
                if not bairro:
                    raise ValueError(
                        'o nome do Bairro não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in bairro):
                    raise ValueError(
                        'O nome do Bairro deve conter apenas letras e espaços!')
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
                    raise ValueError(
                        'O Número deve conter apenas digitos numéricos!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        # Cadastro veiculo
        limpar()
        cabecalho('CADASTRO VEICULO')
        while True:
            try:
                v_modelo = str(input('MODELO: ')).strip()
                if not v_modelo:
                    raise ValueError(
                        'o Modelo do veiculo não pode ser vazio ou conter apenas espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                v_marca = str(input('MARCA: ')).strip()
                if not v_marca:
                    raise ValueError(
                        'A Marca do veiculo não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in v_marca):
                    raise ValueError(
                        'A Marca do veiculo deve conter apenas letras e espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                v_ano = str(input('ANO: ')).strip()
                if not v_ano:
                    raise ValueError('O Ano não pode ser vazio!')
                if not v_ano.isdigit():
                    raise ValueError('O Ano deve conter apenas números!')
                if len(v_ano) != 4:  # Ano deve ter 4 dígitos
                    raise ValueError('O Ano deve ter 4 dígitos!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                v_cor = str(input('COR: ')).strip()
                if not v_cor:
                    raise ValueError(
                        'A Marca do veiculo não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in v_cor):
                    raise ValueError(
                        'A Marca do veiculo deve conter apenas letras e espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        # SERVIÇOS
        limpar()
        cabecalho('CADASTRO SERVIÇO')

        while True:
            try:
                servico = str(input(f'SERVIÇO: ')).strip()
                if not servico:
                    raise ValueError(
                        'o Serviço não pode ser vazio ou conter apenas espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                descricao_servico = str(input('DESCREVA O SERVIÇO: ')).strip()
                if not descricao_servico:
                    raise ValueError(
                        'A descrição do serviço não pode ser vazia ou conter apenas espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                data_inicio = str(
                    input('DATA DE INICIO: (**/**/****) ')).strip()
                if not data_inicio:
                    raise ValueError(
                        'A data de inicio não pode ser vazia ou conter apenas espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                # Mantém como string e remove espaços em volta
                prazo = str(
                    input('PRAZO EM DIAS PARA CONCLUSÃO DO SERVIÇO: ')).strip()
                if not prazo:
                    raise ValueError('O Prazo não pode ser vazio!')
                if not prazo.isdigit():  # Verifica se todos os caracteres são dígitos
                    raise ValueError('O Prazo deve conter apenas números!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break  # interrompe o laço

        while True:
            try:
                orcamento_str = str(input(f'ORÇAMENTO DO SERVIÇO: R$')).strip()
                if not orcamento_str:
                    raise ValueError('O Orçamento não pode ser vazio!')

                orcamento = float(orcamento_str.replace(
                    ',', '.'))  # Tentativa de conversão

                # Verificação de valor negativo
                if orcamento < 0:
                    raise ValueError('O Orçamento não pode ser negativo!')

            except ValueError:
                print(
                    'ERRO: Por favor, insira um valor numérico válido para o orçamento!')
            else:
                print(f'Dado registrado com sucesso: R$ {orcamento:.2f}')
                break  # Interrompe o laço

        # lista de peças
        limpar()
        cabecalho('LISTA DE PEÇAS')

        peca = str(input('PEÇA(S) A SER(EM) UTILIZADA(S): '))

        valor = int(input('VALOR DA PEÇA: R$'))

        # Chamada da SubClasse
        pausar()
        limpar()
        tudo = pecas(nome, cpf, cidade, estado, rua, bairro, numero, v_modelo,
                     v_marca, v_ano, v_cor, servico, orcamento, peca, quantidade, valor)
        cabecalho('REVISE OS DADOS!')
        tudo.print_pecas()
        tudo.exportar_para_csv()
        pausar()

    elif opcao == '2':
        limpar()
        revisar_servico()
        pausar()
    elif opcao == '3':
        limpar()
        print('Sistema Encerrado!')
        pausar()
        limpar()
        print('Obrigado por utilizar nosso Sistema!')
        break
    else:
        print(
            f"{cores[1]}Opção inválida! Por favor, escolha 1, 2 ou 3.{cores[0]}")
        pausar()
