from typing import List, Dict, Tuple

"""
MELHORIA 1: Funções específicas e bem definidas para cada operação bancária
Todas as funções seguem os princípios de responsabilidade única
"""

def saque(*, saldo: float, valor: float, extrato: str, limite: float, 
          numero_saques: int, limite_saques: int) -> Tuple[float, str, int]:
    """
    Realiza operação de saque na conta bancária.
    
    CARACTERÍSTICA: Usa apenas Keyword Arguments (apenas por nome)
    Isso garante clareza ao chamar a função e evita erros de posição
    
    Args:
        saldo: Saldo atual da conta
        valor: Valor a ser sacado
        extrato: Histórico de transações
        limite: Limite máximo por saque
        numero_saques: Número de saques já realizados
        limite_saques: Limite máximo de saques
        
    Returns:
        Tuple contendo saldo atualizado, extrato atualizado e número de saques atualizado
    """
    # Validações de regras de negócio
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    # Controle de fluxo baseado nas validações
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        # Operação bem-sucedida - atualiza todos os dados
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def deposito(saldo: float, valor: float, extrato: str, /) -> Tuple[float, str]:
    """
    Realiza operação de depósito na conta bancária.
    
    CARACTERÍSTICA: Usa apenas Positional Arguments (apenas por posição)
    Isso é indicado para funções simples onde a ordem dos parâmetros é óbvia
    
    Args:
        saldo: Saldo atual da conta (positional only)
        valor: Valor a ser depositado (positional only)
        extrato: Histórico de transações (positional only)
        
    Returns:
        Tuple contendo saldo atualizado e extrato atualizado
    """
    if valor > 0:
        # Depósito válido - atualiza saldo e extrato
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def extrato(saldo: float, /, *, extrato: str) -> None:
    """
    Exibe o extrato bancário com todas as movimentações.
    
    CARACTERÍSTICA: Usa Positional e Keyword Arguments (misto)
    - saldo: positional only (obrigatório e fixo)
    - extrato: keyword only (para clareza)
    
    Args:
        saldo: Saldo atual da conta (positional only)
        extrato: Histórico de transações (keyword only)
    """
    print("\n================ EXTRATO ================")
    # Mostra mensagem personalizada se não houver movimentações
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


"""
MELHORIA 2: Sistema de gerenciamento de usuários e contas
Permite múltiplos usuários e contas no sistema
"""

def criar_usuario(usuarios: List[Dict]) -> None:
    """
    Cria um novo usuário no sistema.
    
    MELHORIA: Sistema de cadastro com validação de CPF único
    Armazena usuários em lista de dicionários para fácil acesso
    
    Args:
        usuarios: Lista de usuários existentes (passada por referência)
    """
    cpf = input("Informe o CPF (somente números): ")
    
    # Valida se usuário já existe pelo CPF
    usuario_existente = filtrar_usuario(cpf, usuarios)
    if usuario_existente:
        print("Já existe usuário com esse CPF!")
        return
    
    # Coleta dados completos do usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    # Adiciona novo usuário à lista
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf: str, usuarios: List[Dict]) -> Dict:
    """
    Filtra usuário por CPF.
    
    FUNÇÃO AUXILIAR: Usada em múltiplos lugares do sistema
    Centraliza a lógica de busca por CPF
    
    Args:
        cpf: CPF do usuário a ser filtrado
        usuarios: Lista de usuários
        
    Returns:
        Usuário encontrado ou None se não existir
    """
    # Busca eficiente usando list comprehension
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia: str, numero_conta: int, usuarios: List[Dict]) -> Dict:
    """
    Cria uma nova conta bancária.
    
    MELHORIA: Vinculação automática com usuário existente
    Número de conta sequencial gerenciado automaticamente
    
    Args:
        agencia: Número da agência (fixo "0001")
        numero_conta: Número da conta (sequencial)
        usuarios: Lista de usuários existentes
        
    Returns:
        Dicionário com os dados da conta criada ou None se falhar
    """
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        # Cria conta com todos os dados necessários
        return {
            "agencia": agencia, 
            "numero_conta": numero_conta, 
            "usuario": usuario,
            "saldo": 0,                    # Saldo inicial zero
            "limite": 500,                 # Limite por saque
            "extrato": "",                 # Extrato vazio inicialmente
            "numero_saques": 0,            # Contador de saques
            "LIMITE_SAQUES": 3             # Limite máximo de saques
        }
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")
    return None


"""
MELHORIA 3: Sistema de busca e seleção de contas por número
Interface mais realista - usuário digita o número da conta diretamente
"""

def buscar_conta_por_numero(numero_conta: int, contas: List[Dict]) -> Dict:
    """
    Busca uma conta pelo número.
    
    MELHORIA: Permite acesso direto à conta pelo número
    Similar a sistemas bancários reais
    
    Args:
        numero_conta: Número da conta a ser buscada
        contas: Lista de contas cadastradas
        
    Returns:
        Conta encontrada ou None se não existir
    """
    # Busca linear - eficiente para quantidade razoável de contas
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    return None


def movimentar_conta(contas: List[Dict]) -> Dict:
    """
    Pede o número da conta para movimentação.
    
    MELHORIA PRINCIPAL: Interface que pede número da conta diretamente
    Mais intuitivo e realista que seleção por lista
    
    Args:
        contas: Lista de contas cadastradas
        
    Returns:
        Conta selecionada ou None se não encontrada
    """
    if not contas:
        print("Nenhuma conta cadastrada.")
        return None
    
    try:
        # Solicita número da conta diretamente
        numero_conta = int(input("\nInforme o número da conta: "))
        conta = buscar_conta_por_numero(numero_conta, contas)
        
        if conta:
            # Confirmação com dados da conta
            print(f"Conta {numero_conta} selecionada - Titular: {conta['usuario']['nome']}")
            return conta
        else:
            print(f"Conta {numero_conta} não encontrada!")
            return None
            
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Por favor, digite um número válido.")
        return None


def listar_contas(contas: List[Dict]) -> None:
    """
    Lista todas as contas cadastradas.
    
    MELHORIA: Mostra informações completas incluindo saldo
    Útil para usuário saber quais contas existem e seus números
    
    Args:
        contas: Lista de contas a serem exibidas
    """
    if not contas:
        print("Não há contas cadastradas.")
        return
    
    print("\n================ CONTAS CADASTRADAS ================")
    for conta in contas:
        # Formatação clara das informações da conta
        linha = f"""
            Agência:\t{conta['agencia']}
            Conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Saldo:\t\tR$ {conta['saldo']:.2f}
        """
        print(linha)
    print("===================================================")


"""
MELHORIA 4: Função principal reorganizada e mais clara
Gerencia todo o fluxo do sistema bancário
"""

def main():
    """
    Função principal do sistema bancário.
    
    MELHORIA: Fluxo completo com todas as operações
    - Gerenciamento de usuários e contas
    - Operações bancárias por conta específica
    - Interface de menu intuitiva
    """
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair

    => """
    
    # Configurações do sistema
    AGENCIA = "0001"  # Agência fixa conforme requisitos
    
    # Estruturas de dados principais
    usuarios = []      # Lista de usuários cadastrados
    contas = []        # Lista de contas criadas
    proximo_numero_conta = 1  # Contador para números de conta sequenciais

    # Loop principal do sistema
    while True:
        opcao = input(menu).strip().lower()

        # DEPÓSITO - Melhoria: Seleção de conta por número
        if opcao == "d":
            print("\n=== DEPÓSITO ===")
            conta = movimentar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta['saldo'], conta['extrato'] = deposito(
                    conta['saldo'], valor, conta['extrato']
                )

        # SAQUE - Melhoria: Seleção de conta por número
        elif opcao == "s":
            print("\n=== SAQUE ===")
            conta = movimentar_conta(contas)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta['saldo'], conta['extrato'], conta['numero_saques'] = saque(
                    saldo=conta['saldo'],
                    valor=valor,
                    extrato=conta['extrato'],
                    limite=conta['limite'],
                    numero_saques=conta['numero_saques'],
                    limite_saques=conta['LIMITE_SAQUES']
                )

        # EXTRATO - Melhoria: Seleção de conta por número
        elif opcao == "e":
            print("\n=== EXTRATO ===")
            conta = movimentar_conta(contas)
            if conta:
                extrato(conta['saldo'], extrato=conta['extrato'])

        # NOVO USUÁRIO - Funcionalidade adicionada
        elif opcao == "nu":
            print("\n=== NOVO USUÁRIO ===")
            criar_usuario(usuarios)

        # NOVA CONTA - Funcionalidade adicionada
        elif opcao == "nc":
            print("\n=== NOVA CONTA ===")
            conta = criar_conta(AGENCIA, proximo_numero_conta, usuarios)
            if conta:
                contas.append(conta)
                proximo_numero_conta += 1
                print(f"Conta {conta['numero_conta']} criada com sucesso!")

        # LISTAR CONTAS - Funcionalidade adicionada
        elif opcao == "lc":
            listar_contas(contas)

        # SAIR DO SISTEMA
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema!")
            break

        # TRATAMENTO DE OPÇÃO INVÁLIDA
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()