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
    def __init__(self, dados_pessoa):
        self.nome = dados_pessoa['nome']
        self.cpf = dados_pessoa['cpf']
        self.cidade = dados_pessoa['cidade']
        self.estado = dados_pessoa['estado']
        self.rua = dados_pessoa['rua']
        self.bairro = dados_pessoa['bairro']
        self.numero = dados_pessoa['numero']

    def sobre_cadastro_pessoa(self):
        return (f'NOME: {self.nome}\nCPF: {self.cpf}\nCIDADE: {self.cidade}\nESTADO: {self.estado}\nRUA: {self.rua}\nBAIRRO: {self.bairro}\nNUMERO: {self.numero}')

# SubClasse (dados específicos: v_modelo, v_marca, v_ano, v_cor)


class veiculo(pessoal):
    def __init__(self, dados_pessoa, dados_veiculo):
        super().__init__(dados_pessoa)
        self.v_modelo = dados_veiculo['modelo']
        self.v_marca = dados_veiculo['marca']
        self.v_ano = dados_veiculo['ano']
        self.v_cor = dados_veiculo['cor']

    def sobre_cadastro_veiculo(self):
        return (f'MODELO: {self.v_modelo}\nMARCA: {self.v_marca}\nANO: {self.v_ano}\nCOR: {self.v_cor}')

# Subclasse Serviço


class servicos(veiculo):
    def __init__(self, dados_pessoa, dados_veiculo, dados_servico):
        super().__init__(dados_pessoa, dados_veiculo)
        self.servico = dados_servico['servico']
        self.descricao_servico = dados_servico['descricao']
        self.data_inicio = dados_servico['data_inicio']
        self.prazo = dados_servico['prazo']
        self.orcamento = dados_servico['orcamento']

    def sobre_servicos(self):
        return (f'SERVIÇO: {self.servico}\nDESCRÇÃO: {self.descricao_servico}\nDATA DE INÍCIO: {self.data_inicio}\nPRAZO EM DIAS: {self.prazo}\nORÇAMENTO: {self.orcamento}')


class pecas(servicos):
    def __init__(self, dados_pessoa, dados_veiculo, dados_servico, lista_pecas):
        super().__init__(dados_pessoa, dados_veiculo, dados_servico)
        self.lista_pecas = lista_pecas
        
    
    def print_pecas(self):
        cabecalho('DADOS PESSOAIS')
        print(f'{super().sobre_cadastro_pessoa()}')
        cabecalho('DADOS VEICULO')
        print(f'{super().sobre_cadastro_veiculo()}')
        cabecalho('SERVIÇOS')
        print(f'{super().sobre_servicos()}')
        cabecalho('PECAS')
        if self.lista_pecas:  # Verifica se a lista não está vazia
            for peca in self.lista_pecas:
                print(f"NOME: {peca['nome']}")
                print(f"MARCA: {peca['marca']}")
                print(f"VALOR: R$ {peca['valor']}")
                print(f"HISTÓRICO: {peca['historico']}")
                print(f"DESCRIÇÃO: {peca['descricao']}")
                print('-' * 20)
            valor_total_pecas = sum(peca['valor'] for peca in self.lista_pecas)
            orcamento_total = self.orcamento + valor_total_pecas
            cabecalho('ORÇAMENTO TOTAL')
            print(f"ORÇAMENTO TOTAL: R$ {orcamento_total:.2f}")
        else:
            print("Nenhuma peça cadastrada.")

    def sobre_pecas(self):
        return (f'PECAS: {self.peca}\nVALOR: {self.valor}')
    # quero que aqui seja uma funcao que crie arquivo csv com o nome herdado da classe principal cadastropessoas

    def exportar_para_csv(self):
        # Define o nome do arquivo baseado no nome do cliente
        nome_arquivo = f"{self.nome.upper().replace(' ', '_')}_servico.csv"

       
        # Calcula o valor total
        valor_total_pecas = 0
        for peca in self.lista_pecas:
            valor_total_pecas += peca['valor']
        orcamento_total = self.orcamento + valor_total_pecas
        
        # Criar um DataFrame para armazenar os dados das peças
        df_pecas = pd.DataFrame(self.lista_pecas)  # Cada peça se torna uma linha

        # Adicionar as colunas com os dados do cliente, veículo e serviço
        df_pecas['Nome_Cliente'] = self.nome
        df_pecas['CPF'] = self.cpf
        df_pecas['Cidade'] = self.cidade
        df_pecas['Estado'] = self.estado
        df_pecas['Rua'] = self.rua
        df_pecas['Bairro'] = self.bairro
        df_pecas['Numero'] = self.numero
        df_pecas['Modelo_Veiculo'] = self.v_modelo
        df_pecas['Marca'] = self.v_marca
        df_pecas['Ano'] = self.v_ano
        df_pecas['Cor'] = self.v_cor
        df_pecas['Servico'] = self.servico
        df_pecas['Descricao_Servico'] = self.descricao_servico
        df_pecas['Data_Inicio'] = self.data_inicio
        df_pecas['Prazo'] = self.prazo
        df_pecas['Orcamento'] = self.orcamento
         # ... adicionar as outras colunas

        # Criar um DataFrame inicial com os dados do cliente, veículo e serviço
        df_inicial = pd.DataFrame({'Nome_Cliente': [self.nome], 'CPF': [self.cpf], 'Cidade': [self.cidade], 'Estado': [self.estado], 'Rua': [self.rua], 'Bairro': [self.bairro], 'Numero': [self.numero],
                                   'Modelo_Veiculo': [self.v_modelo], 'Marca': [self.v_marca], 'Ano': [self.v_ano], 'Cor': [self.v_cor],
                                   'Servico': [self.servico], 'Descricao_Servico': [self.descricao_servico], 'Data_Inicio': [self.data_inicio], 'Prazo': [self.prazo], 'Orcamento': [self.orcamento]})

        # Concatenar os DataFrames
        df = pd.concat([df_inicial, df_pecas], ignore_index=True)

        # Envia o Orçamento Total
        df['Orcamento_Total'] = orcamento_total

        # Salvar o DataFrame para o CSV
        df.to_csv(nome_arquivo, index=False)

# se usuario selecionar a opção 2, função de revisar o pedido
def revisar_servico():
    #solicita o nome do cliente
    cliente_nome = str(input("Digite o nome do cliente para revisar o serviço: ")).strip().upper().replace(" ", "_")
    arquivo_csv = f"{cliente_nome}_servico.csv" # Cria o arquivo com o nome do cliente_servico.csv
    if os.path.exists(arquivo_csv): # Verifica se o arquivo foi criado
        df = pd.read_csv(arquivo_csv) # data frame pandas para leitura dos dados

        cabecalho('DADOS PESSOAIS')
        print(f'NOME: {df["Nome_Cliente"][0]}')
        print(f'CPF: {df["CPF"][0]}')
        print(f'CIDADE: {df["Cidade"][0]}')
        print(f'ESTADO: {df["Estado"][0]}')
        print(f'RUA: {df["Rua"][0]}')
        print(f'BAIRRO: {df["Bairro"][0]}')
        print(f'NUMERO: {df["Numero"][0]}')

        cabecalho('DADOS VEICULO')
        print(f'MODELO: {df["Modelo_Veiculo"][0]}')
        print(f'MARCA: {df["Marca"][0]}')
        print(f'ANO: {df["Ano"][0]}')
        print(f'COR: {df["Cor"][0]}')

        cabecalho('SERVIÇOS')
        print(f'SERVIÇO: {df["Servico"][0]}')
        print(f'DESCRIÇÃO: {df["Descricao_Servico"][0]}')
        print(f'DATA DE INÍCIO: {df["Data_Inicio"][0]}')
        print(f'PRAZO: {df["Prazo"][0]}')
        print(f'ORÇAMENTO: {df["Orcamento"][0]}')

        cabecalho('PEÇAS')
        for index, row in df.iterrows(): # percore as linhas e colunas
            if index == 0:  # Pula a primeira linha (já exibida), retorna para as demais linhas que preenchem as informações das peças
                continue
            print(f"PEÇA {index}:")
            print(f"NOME: {row['nome']}")
            print(f"MARCA: {row['marca']}")
            print(f"VALOR: R$ {row['valor']}")
            print(f"HISTÓRICO: {row['historico']}")
            print(f"DESCRIÇÃO: {row['descricao']}")
            print('-' * 20)
        cabecalho('ORÇAMENTO TOTAL')
        print(f'ORÇAMENTO TOTAL: {df['Orcamento_Total'][0]}')
    else:
        print(f"{cores[1]}Erro: Arquivo para o cliente '{cliente_nome}' não encontrado!{cores[0]}")

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
                cpf = str(input('CPF (somente números, sem espaços ou pontos): ')).strip()
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

        # Dados da Pessoa
        dados_pessoa = {
            'nome': nome,
            'cpf': cpf,
            'cidade': cidade,
            'estado': estado,
            'rua': rua,
            'bairro': bairro,
            'numero': numero
        }       

        # Cadastro veiculo
        limpar()
        cabecalho('CADASTRO VEICULO')
        while True:
            try:
                v_modelo = str(input('MODELO: ')).strip()
                if not v_modelo:
                    raise ValueError('o Modelo do veiculo não pode ser vazio ou conter apenas espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                v_marca = str(input('MARCA: ')).strip()
                if not v_marca:
                    raise ValueError('A Marca do veiculo não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in v_marca):
                    raise ValueError('A Marca do veiculo deve conter apenas letras e espaços!')
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
                    raise ValueError('A Marca do veiculo não pode ser vazio ou conter apenas espaços!')
                if not all(x.isalpha() or x.isspace() for x in v_cor):
                    raise ValueError('A Marca do veiculo deve conter apenas letras e espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break
       
        # Dados do veiculo        
        dados_veiculo = {
            'modelo': v_modelo,
            'marca': v_marca,
            'ano': v_ano,
            'cor': v_cor
        }

        # SERVIÇOS
        limpar()
        cabecalho('CADASTRO SERVIÇO')

        while True:
            try:
                servico = str(input(f'SERVIÇO: ')).strip()
                if not servico:
                    raise ValueError('o Serviço não pode ser vazio ou conter apenas espaços!')
            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break

        while True:
            try:
                descricao_servico = str(input('DESCREVA O SERVIÇO: ')).strip()
                if not descricao_servico:
                    raise ValueError('A descrição do serviço não pode ser vazia ou conter apenas espaços!')
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
                    raise ValueError('A data de inicio não pode ser vazia ou conter apenas espaços!')
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

                orcamento = float(orcamento_str.replace(',', '.'))  # Tentativa de conversão

                # Verificação de valor negativo
                if orcamento < 0:
                    raise ValueError('O Orçamento não pode ser negativo!')

            except ValueError as e:
                print(f'{cores[1]}ERRO: {e}{cores[0]}')
            else:
                print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                break  # interrompe o laço
        
        # Dados do serviço
        dados_servico = {
            'servico': servico,
            'descricao': descricao_servico,
            'data_inicio': data_inicio,
            'prazo': prazo,
            'orcamento': orcamento
        }
        
        # lista de peças
        limpar()
        cabecalho('LISTA DE PEÇAS')
        lista_pecas = []
        while True:
            while True:
                try:
                    Nome = str(input('NOME DA PEÇA: ')).strip()
                    if not Nome:
                        raise ValueError('A Nome da Peça não pode ser vazia ou conter apenas espaços!')
                except ValueError as e:
                    print(f'{cores[1]}ERRO: {e}{cores[0]}')
                else:
                    print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                    break
            
            while True:
                try:
                    Marca = str(input('MARCA DA PEÇA: ')).strip()
                    if not Marca:
                        raise ValueError('A Marca da Peça não pode ser vazia ou conter apenas espaços!')
                except ValueError as e:
                    print(f'{cores[1]}ERRO: {e}{cores[0]}')
                else:
                    print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                    break
            
            while True:
                try:
                    Valor_str = str(input(f'ORÇAMENTO DA PEÇA: R$')).strip()
                    if not Valor_str:
                        raise ValueError('O Orçamento da Peça não pode ser vazio!')

                    Valor = float(Valor_str.replace(',', '.'))  # Tentativa de conversão
                    # Verificação de valor negativo
                    if Valor < 0:
                        raise ValueError('O Orçamento da Peça não pode ser negativo!')
                except ValueError as e:
                    print(f'{cores[1]}ERRO: {e}{cores[0]}')
                else:
                    print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                    break  
            while True:
                try:
                    historico = str(input('HISTÓRICO DE USO (NOVA/USADA): ')).strip().upper()
                    if not historico:
                        raise ValueError('O Histórico não pode ser vazio!')
                    if historico in 'NOVA':
                        historico = 'NOVA'
                    elif historico in "USADA":
                        historico = 'USADA'
                    else:
                        raise ValueError('O Hístorico deve ser apenas NOVA/USADA')
                except ValueError as e:
                    print(f'{cores[1]}ERRO: {e}{cores[0]}')
                else:
                    print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                    break
            
            while True:
                try:
                    Descricao = str(input('DESCRIÇÃO: ')).strip()
                    if not Descricao:
                        raise ValueError('A Descrição não pode ser vazia ou conter apenas espaços!')
                except ValueError as e:
                    print(f'{cores[1]}ERRO: {e}{cores[0]}')
                else:
                    print(f'{cores[2]}Dado registrado com sucesso!!{cores[0]}')
                    break
            # Dados Peças
            peca = {
                'nome': Nome,
                'marca': Marca,
                'valor': Valor,
                'historico': historico,
                'descricao': Descricao
            }
            lista_pecas.append(peca)

            continuar = input('Deseja cadastrar outra peça? (s/n): ').lower()
            if continuar != 's':
                break

        # Chamada da SubClasse
        pausar()
        limpar()
        tudo = pecas(dados_pessoa, dados_veiculo, dados_servico, lista_pecas)
        cabecalho('REVISE OS DADOS!')
        tudo.print_pecas()
        tudo.exportar_para_csv()
        pausar()
    
    # Opção de Revisar cadastro
    elif opcao == '2':
        limpar()
        revisar_servico()
        pausar()
    
    # Opção de saida
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