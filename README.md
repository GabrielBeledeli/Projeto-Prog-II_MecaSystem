# Sistema de Gerenciamento de Oficina Mecânica
# MecaSystem

Este sistema foi desenvolvido para auxiliar no gerenciamento de uma oficina mecânica. Ele permite o cadastro de dados pessoais dos clientes, informações sobre veículos, serviços realizados e peças utilizadas, com geração de orçamentos detalhados e a capacidade de exportar os dados para arquivos CSV.

## Funcionalidades

- Cadastro de **clientes**, com informações como nome, CPF, endereço, etc.
- Cadastro de **veículos**, com dados como modelo, marca, ano e cor.
- Cadastro de **serviços** realizados, incluindo descrição, data de início, prazo e orçamento.
- Cadastro de **peças** utilizadas no serviço, com informações sobre nome, marca, valor, histórico e descrição.
- Geração de **orçamento total** com a soma dos serviços e peças.
- Exportação dos dados para arquivos **CSV**.
- Função de **revisão** do serviço realizado, com leitura do arquivo CSV gerado anteriormente.

## Estrutura do Projeto

O sistema é composto pelas seguintes classes:

### 1. `pessoal`

Classe base que armazena os dados pessoais do cliente, como nome, CPF, endereço, etc.

### 2. `veiculo`

Herda da classe `pessoal` e adiciona dados sobre o veículo do cliente, como modelo, marca, ano e cor.

### 3. `servicos`

Herda da classe `veiculo` e adiciona informações sobre os serviços realizados, como descrição, data de início, prazo e orçamento.

### 4. `pecas`

Herda da classe `servicos` e adiciona informações sobre as peças utilizadas no serviço, incluindo nome, marca, valor, histórico e descrição.

## Requisitos

- Python 3.x
- Pandas (para exportação e leitura de arquivos CSV)

## Como usar

1. **Cadastro de Dados:**
   - O sistema solicita as informações do cliente, veículo, serviço e peças.
   
2. **Revisão de Serviços:**
   - Após realizar um serviço, o sistema gera um arquivo CSV.
   - Você pode revisar o serviço utilizando a função de revisão, que carrega os dados do arquivo CSV.

3. **Exportação para CSV:**
   - O sistema exporta os dados para um arquivo CSV que pode ser facilmente manipulado ou consultado.

## Exemplo de Uso

```python
# Exemplo de como cadastrar os dados e gerar o orçamento

# Dados do cliente
dados_cliente = {
    'nome': 'João Silva',
    'cpf': '123.456.789-00',
    'cidade': 'São Paulo',
    'estado': 'SP',
    'rua': 'Rua A',
    'bairro': 'Centro',
    'numero': '123'
}

# Dados do veículo
dados_veiculo = {
    'modelo': 'Fusca',
    'marca': 'Volkswagen',
    'ano': '1985',
    'cor': 'Azul'
}

# Dados do serviço
dados_servico = {
    'servico': 'Troca de óleo',
    'descricao': 'Troca de óleo do motor',
    'data_inicio': '2024-11-10',
    'prazo': 1,
    'orcamento': 200.0
}

# Cadastro de peças
pecas = [
    {'nome': 'Óleo 10W-40', 'marca': 'Castrol', 'valor': 50.0, 'historico': 'Novo', 'descricao': 'Óleo de motor'},
    {'nome': 'Filtro de óleo', 'marca': 'Fram', 'valor': 30.0, 'historico': 'Novo', 'descricao': 'Filtro de óleo de motor'}
]

# Criação do objeto 'pecas'
cliente_pecas = pecas(dados_cliente, dados_veiculo, dados_servico, pecas)

# Imprimir todos os dados
cliente_pecas.print_pecas()

# Exportar os dados para CSV
cliente_pecas.exportar_para_csv()
