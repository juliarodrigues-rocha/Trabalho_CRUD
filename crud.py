import re
from datetime import datetime

# Padrões de validação
padrao_de_telefone = re.compile(r'^(?:\(([0-9]{2})\) )?[0-9]{4,5}-[0-9]{4}$')
padrao_de_celular = re.compile(r'^(?:\(([0-9]{2})\) )?9[0-9]{4}-[0-9]{4}$')
padrao_de_nome = re.compile(r'^[A-Z][a-z]*(?: [A-Z][a-z]*)*$')
padrao_de_endereco = re.compile(r'^[A-Z][a-zA-ZÀ-ÿ\s]+\s\d+[a-zA-ZÀ-ÿ]*$')
padrao_de_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# DDDs válidos no Brasil (11-99, exceto reservados)
ddd_validos = set(range(11, 100)) - {20, 23, 25, 26, 29, *range(30, 40), 40, 50, 70, 90}

def validar_ddd(ddd):
    try:
        return int(ddd) in ddd_validos
    except ValueError:
        return False

def validar_telefone(numero):
    match = padrao_de_telefone.match(numero)
    if not match:
        return False
    ddd = match.group(1)
    if ddd and not validar_ddd(ddd):
        return False
    return True

def validar_celular(numero):
    match = padrao_de_celular.match(numero)
    if not match:
        return False
    ddd = match.group(1)
    if ddd and not validar_ddd(ddd):
        return False
    return True

def validar_data_aniversario(data_str):
    try:
        dia, mes = map(int, data_str.split('/'))
        if not (1 <= mes <= 12):
            return False
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
        if mes == 2 and dia > 29:
            return False
        return 1 <= dia <= 31
    except:
        return False

def apresenteSe():
    print('+-------------------------------------------------------------------------------+')
    print('|                                                                               |')
    print('|         AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS           |')
    print('|                                                                               |')
    print('|  Júlia Rodrigues da Rocha RA:25005897 & Rafael Ferreira Lucietto RA:25004572  |')
    print('|                                                                               |')
    print('|                       Versão 3.0 de 20/maio/2025                              |')
    print('|                                                                               |')
    print('+-------------------------------------------------------------------------------+')

def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao).strip()
        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True
    return txt

def opcaoEscolhida(menu):
    print()
    opcoesValidas = []
    
    for i, opcao in enumerate(menu, start=1):
        print(f"{i}) {opcao}")
        opcoesValidas.append(str(i))
    
    print()
    while True:
        opcao = input('Qual é a sua opção? ').strip()
        if opcao in opcoesValidas:
            return int(opcao)
        print('Opção inválida - Favor redigitar...')

def ondeEsta(nome, agd):
    inicio = 0
    final = len(agd)-1

    while inicio <= final:
        meio = (inicio + final) // 2
        if agd[meio][0].upper() == nome.upper():
            return [True, meio]
        elif agd[meio][0].upper() < nome.upper():
            inicio = meio + 1
        else:
            final = meio - 1

    return [False, inicio]

def cadastrar(agd):
    while True:
        nome = input("\nInsira um nome ou 'Cancela' para sair do cadastro: ").strip()
        
        if nome.upper() == 'CANCELA':
            print("\nCadastro cancelado")
            return

        if not padrao_de_nome.match(nome):
            print("Nome inválido! Deve começar com letra maiúscula e conter apenas letras e espaços.")
            continue

        validacao = ondeEsta(nome, agd)
        if validacao[0]:
            print("Nome já existe! Favor digitar outro...")
            continue

        # Validação da data de aniversário
        while True:
            aniversario = input("Insira a data de aniversário (DD/MM): ").strip()
            if validar_data_aniversario(aniversario):
                break
            print("Data inválida! Formato esperado: DD/MM (dia 1-31, mês 1-12)")

        # Validação do endereço
        while True:
            end = input("Insira o endereço (Ex: Rua das Flores 123): ").strip()
            if padrao_de_endereco.match(end):
                break
            print("Endereço inválido! Deve começar com letra maiúscula e terminar com número.")

        # Validação do telefone
        while True:
            telefone = input("Digite o telefone fixo ((xx) xxxx-xxxx ou xxxx-xxxx): ").strip()
            if validar_telefone(telefone):
                break
            print("Telefone inválido. Formato esperado: (xx) xxxx-xxxx ou xxxx-xxxx com DDD válido (11-99, exceto 20,23,25,26,29,30-39,40,50,70,90)")

        # Validação do celular
        while True:
            celular = input("Digite o celular ((xx) 9xxxx-xxxx): ").strip()
            if validar_celular(celular):
                break
            print("Celular inválido. Formato esperado: (xx) 9xxxx-xxxx com DDD válido (11-99, exceto 20,23,25,26,29,30-39,40,50,70,90)")

        # Validação do email
        while True:
            email = input("Insira o email (Ex: nome@provedor.com): ").strip()
            if padrao_de_email.match(email):
                break
            print("Email inválido! Formato esperado: nome@provedor.com")

        contato = [nome, aniversario, end, telefone, celular, email]
        agenda.insert(validacao[1], contato)
        print("\nCadastro realizado com sucesso!")
        return

def procurar(agd):
    if len(agd) == 0:
        print("\nA agenda está vazia. Não há contatos para procurar.")
        return
        
    while True:
        nome = input("\nInsira um nome ou digite 'Cancela' para sair: ").strip()
        
        if nome.upper() == 'CANCELA':
            print("\nProcura cancelada")
            return
            
        validacao = ondeEsta(nome, agd)
        
        if not validacao[0]:
            print("Nome não encontrado! Tente novamente.")
            continue

        contato = agd[validacao[1]]
        print("\nContato encontrado:")
        print(f"Nome: {contato[0]}")
        print(f"Aniversário: {contato[1]}")
        print(f"Endereço: {contato[2]}")
        print(f"Telefone: {contato[3]}")
        print(f"Celular: {contato[4]}")
        print(f"E-mail: {contato[5]}")
        return

def atualizar(agd):
    if len(agd) == 0:
        print("\nA agenda está vazia. Não há contatos para atualizar.")
        return
        
    while True:
        nome = input("\nInsira um nome para atualizar ou 'Cancela' para sair: ").strip()
        if nome.upper() == 'CANCELA':
            print("\nAtualização cancelada")
            return

        validacao = ondeEsta(nome, agd)
        if not validacao[0]:
            print("Nome não encontrado! Tente novamente.")
            continue

        indice = validacao[1]
        contato = agd[indice]
        
        while True:
            print("\nSelecione o campo para atualizar:")
            opcao = opcaoEscolhida([
                'Aniversário', 
                'Endereço', 
                'Telefone', 
                'Celular', 
                'Email', 
                'Finalizar atualização'
            ])

            if opcao == 6:
                print("\nAtualizações concluídas.")
                return

            campo = opcao - 1
            valor_atual = contato[opcao]
            
            print(f"\nValor atual: {valor_atual}")
            novo_valor = input("Digite o novo valor ou 'cancela' para manter: ").strip()
            
            if novo_valor.upper() == 'CANCELA':
                print("Alteração cancelada.")
                continue
                
            # Validações específicas para cada campo
            if opcao == 1:  # Aniversário
                if not validar_data_aniversario(novo_valor):
                    print("Data inválida! Formato DD/MM com valores válidos.")
                    continue
                    
            elif opcao == 2:  # Endereço
                if not padrao_de_endereco.match(novo_valor):
                    print("Endereço inválido! Deve começar com letra maiúscula e terminar com número.")
                    continue
                    
            elif opcao == 3:  # Telefone
                if not validar_telefone(novo_valor):
                    print("Telefone inválido. Formato esperado: (xx) xxxx-xxxx ou xxxx-xxxx com DDD válido (11-99, exceto 20,23,25,26,29,30-39,40,50,70,90)")
                    continue
                    
            elif opcao == 4:  # Celular
                if not validar_celular(novo_valor):
                    print("Celular inválido. Formato esperado: (xx) 9xxxx-xxxx com DDD válido (11-99, exceto 20,23,25,26,29,30-39,40,50,70,90)")
                    continue
                    
            elif opcao == 5:  # Email
                if not padrao_de_email.match(novo_valor):
                    print("Email inválido! Formato esperado: nome@provedor.com")
                    continue

            agd[indice][opcao] = novo_valor
            print("Campo atualizado com sucesso!")

def listar(agd):
    print()
    if len(agd) == 0:
        print("A agenda está vazia. Não há contatos para listar.")
        return

    print("=========== Lista de contatos cadastrados ===========")
    for i, contato in enumerate(agd, start=1):
        print(f"\nContato {i}:")
        print(f"  Nome:        {contato[0]}")
        print(f"  Aniversário: {contato[1]}")
        print(f"  Endereço:    {contato[2]}")
        print(f"  Telefone:    {contato[3]}")
        print(f"  Celular:     {contato[4]}")
        print(f"  E-mail:      {contato[5]}")

def excluir(agd):
    if len(agd) == 0:
        print("\nA agenda está vazia. Não há contatos para excluir.")
        return
        
    while True:
        nome = input("\nDigite o nome a excluir ou 'Cancela' para desistir: ").strip()
        
        if nome.upper() == 'CANCELA':
            print("\nExclusão cancelada.")
            return

        validacao = ondeEsta(nome, agd)
        if not validacao[0]:
            print("Contato não encontrado. Tente novamente.")
            continue

        indice = validacao[1]
        contato = agd[indice]
        
        print("\nContato encontrado:")
        print(f"  Nome:        {contato[0]}")
        print(f"  Aniversário: {contato[1]}")
        print(f"  Endereço:    {contato[2]}")
        print(f"  Telefone:    {contato[3]}")
        print(f"  Celular:     {contato[4]}")
        print(f"  E-mail:      {contato[5]}")

        confirmar = input("\nTem certeza que deseja excluir este contato? (S/N): ").strip().upper()
        if confirmar == 'S':
            del agd[indice]
            print("\nContato excluído com sucesso!")
            return
        elif confirmar == 'N':
            print("\nExclusão cancelada.")
            return
        else:
            print("\nResposta inválida! Digite apenas S ou N.")

# Programa principal
apresenteSe()
agenda = []

menu = [
    'Cadastrar Contato',
    'Procurar Contato',
    'Atualizar Contato',
    'Listar Contatos',
    'Excluir Contato',
    'Sair do Programa'
]

while True:
    opcao = opcaoEscolhida(menu)

    if opcao == 1:
        cadastrar(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)
    else:  # opcao == 6
        print('\nPROGRAMA ENCERRADO COM SUCESSO!')
        break
