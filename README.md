# sistema_bancario
Sistema de saque, depósito e extrato bancário atualizado para criação de novo usuário e conta.

OBJETIVO GERAL:
Separar as funções existentes de saque, depósito e extrato em funções. 
Deixar o código mais modularizado, e para isso, criar funções para as operações existentes: sacar, 
depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas 
funções novas: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

SEPARAR EM FUNÇÕES
Criar funções para todas as operações do sistema.
Cada função deve ter uma regra na passagem de argumentos. 

SAQUE
A função saque deve receber os argumentos apenas por nome (Keyword Only). 
Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. 
Sugestão de retorno: saldo e extrato.

DEPÓSITO
A função depósito deve receber os argumentos apenas por posição (positional Only).
Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo e extrato.

EXTRATO
A função extrato deve receber os argumentos apenas por posição e nome (positional Only e Keyword Only).
Argumentos posicionais: saldo, argumentos nomeados: extrato.
NOVAS FUNÇÕES PROPOSTAS
Criar duas funções novas: criar usuário e criar conta corrente. Fique à vontade para criar mais funções, exemplo: listar contas.

CRIAR USUÁRIO (CLIENTE)
O programa deve armazenar os usuários em uma lista, onde um usuário é composto por: nome, data de nascimento, cpf e endereço. 
O endereço é uma string com o formato: logradouro, numero, bairro, cidade/sigla do estado. Deve ser armazenado somente os números 
do cpf. Não podemos cadastrar dois usuários com o mesmo cpf.

CRIAR CONTA CORRENTE
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, 
iniciando em 1. O número da agência é fixo “0001”. O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
Para vincular um usuário a uma conta, filtrar a lista de usuários buscando o número do cpf informado para cada usuário da lista.

NOVAS FUNÇÕES ACRESCENTADAS NO SISTEMA

1. Funções de Gerenciamento de Usuários
criar_usuario(usuarios: List[Dict]) -> None
Função completamente NOVA
•	Cadastra novos usuários no sistema
•	Valida CPF único (não permite duplicatas)
•	Armazena: nome, data nascimento, CPF e endereço
•	Adicionada para substituir o sistema de conta única
filtrar_usuario(cpf: str, usuarios: List[Dict]) -> Dict
Função completamente NOVA
•	Busca usuário pelo CPF na lista
•	Retorna o usuário encontrado ou None
•	Função auxiliar usada em múltiplos lugares

2. Funções de Gerenciamento de Contas
criar_conta(agencia: str, numero_conta: int, usuarios: List[Dict]) -> Dict
Função completamente NOVA
•	Cria nova conta corrente vinculada a um usuário
•	Número de conta sequencial automático
•	Agência fixa "0001"
•	Permite múltiplas contas no sistema
listar_contas(contas: List[Dict]) -> None
Função completamente NOVA
•	Exibe todas as contas cadastradas
•	Mostra agência, número da conta, titular e saldo
•	Ajuda usuário a saber quais contas existem

3. Funções de Seleção de Conta (MELHORIA PRINCIPAL)
buscar_conta_por_numero(numero_conta: int, contas: List[Dict]) -> Dict

Função completamente NOVA
•	Busca uma conta específica pelo número
•	Retorna a conta encontrada ou None
•	Base do sistema de seleção por número
movimentar_conta(contas: List[Dict]) -> Dict

Função completamente NOVA
•	MELHORIA PRINCIPAL: Pede para digitar o número da conta
•	Interface mais realista (como bancos reais)
•	Confirma com dados do titular
•	Substitui a seleção por lista

4. Função Principal Expandida
main()
Função EXISTENTE mas completamente MODIFICADA
•	Menu expandido com novas opções
•	Fluxo completo de múltiplas contas
•	Integração de todas as novas funções
•	Gerenciamento completo do sistema

