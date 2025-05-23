import re
padrao_de_telefone = re.compile('^(?:\\([0-9]{2}\\) )?9?[0-9]{4}-[0-9]{4}$')
padrao_de_celular = re.compile('^(?:\\([0-9]{2}\\) )?9?[0-9]{5}-[0-9]{4}$')
padrao_de_nome = re.compile('^[A-Z][a-z]*(?: (?:[A-Z]|[a-z])[a-z]*)*$')
padrao_de_data = re.compile(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$')


def apresenteSe ():
    print('+-------------------------------------------------------------------------------+')
    print('|                                                                               |')
    print('|         AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS           |')
    print('|                                                                               |')
    print('|  Júlia Rodrigues da Rocha RA:25005897 & Rafael Ferreira Lucietto RA:25004572  |')
    print('|                                                                               |')
    print('|                       Versão 2.0 de 20/maio/2025                              |')
    print('|                                                                               |')
    print('+-------------------------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)
        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True
    return txt



def opcaoEscolhida (menu):
    print() #pula linha

    opcoesValidas=[] #lista
    posicao=0 #contador
    while posicao<len(menu): #enquanto a posição for menor que o tamanho do menu
        print (posicao+1,') ',menu[posicao],sep='') #começa printando a posição corretamente, já que está como +1; ent printa assim: 1) posição
        opcoesValidas.append(str(posicao+1)) # coloca na lista opcoesValidas uma string com a posição +1
        posicao+=1 # contador 

    print() #pula linha
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)    






''' Procura nome em agenda e, se achou, retorna: uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna: uma lista contendo False e a posição onde inserir, aquilo que foi buscado, mas nao foi encontrado, mantendo a ordenação da lista. '''
def ondeEsta (nome,agd): #nome fica na posição zero
    inicio = 0
    final =len(agd)-1 #COMO COMEÇA NO ZERO CONTA O ZERO, E ISSO DA PROBLEMA, POR ISSO MENOS 1
    
    while inicio <= final: #então ainda não achamos o nome
        meio=(inicio+final)//2
        
        if agd[meio][0].upper() == nome.upper():
            return [True, meio]
        elif agd[meio][0].upper() < nome.upper():
            inicio = meio + 1 # então o nome esta para a direita, é maior que o meio > 5
        else:
            final = meio - 1 # então o nome esta para a esquerda, é menor que o meio < 5
        
    return [False, inicio] # aqui e caso não ache o nome, então ele nao existe e deve ser inserido nessa posição de inicio
    
    # a função deverá retornar a lista [True,meio] quando encontrar nome procurado ou então a lista [False,inicio], quando não encontrar o nome procurado.
    # busca binária

def validaNome (nome):
    listaPossiveis = ['de', 'da', 'do', 'dos', 'das'] # possíveis nomes que não precisam do maiusculo no começo
    listaNome = nome.split() # lista de cada palavra do nome
    
    for i in range(len(listaNome)): 
        if listaNome[i].lower() in listaPossiveis:
            if i == 0 or i == len(listaNome) - 1: # não entendi direito
                return False
            else:
                continue
        else:
            if not padrao_de_nome.match(listaNome[i]):
                return False
    
def validaData (dia, mes, ano):
    if dia < 0 or dia > 31:
        print("Valor inválido para dia!")  # Só é possível validar o intervalo do dia
        return False
    else:
        if mes < 0 or mes > 12:
            print("Valor inválido para mês!")  # Mês deve estar entre 1 e 12
            return False
        else:
            # Verifica se o mês tem apenas 30 dias
            if dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                print("Valor de dia e de mês incompatíveis um com o outro!")
                return False
            # Verifica o mês de fevereiro
            elif dia > 29 and mes == 2:
                print("Valor de dia e de mês incompatíveis um com o outro!")
                return False
            # Verifica anos antigos
            elif ano < -45:
                print("Este programa não valida datas com anos anteriores a 46 a.C., antes do calendário juliano!")
                return False
            elif ano == 0:
                print("Não existiu ano 0!")
                return False
            # Verifica a transição do calendário juliano para gregoriano
            elif dia >= 5 and dia <= 14 and mes == 10 and ano == 1582:
                print("Este dia não existiu neste mês e ano!")
                return False
            else:
                if ano < 1582:
                    # Ano juliano
                    if ano % 4 == 0:
                        print("Data válida!")  # Ano bissexto juliano
                        return True
                    else:
                        if dia > 28 and mes == 2:
                            print("Valor de dia, mês e ano incompatíveis um com o outro!")
                            return False
                        else:
                            return True  # Ano comum juliano
                else:
                    # Ano gregoriano
                    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
                        print("Data válida!")
                        return True# Ano bissexto gregoriano
                    else:
                        if dia > 28 and mes == 2:
                            print("Valor de dia, mês e ano incompatíveis um com o outro!")
                            return False
                        else:
                            return True  # Ano comum gregoriano

def cadastrar (agd):
    # Ficar solicitando a digitação de um nome de um contato a ser cadastrado na agenda, até que um nome NÃO CADASTRADO seja digitado.
    while True:
        nome = input("Insira um nome ou 'Cancela' para sair do cadastro: ").strip()
        
        if nome.upper() == 'CANCELA':
            print("\nCadastro cancelado")
            return
            
        if not padrao_de_nome.match(nome):
            print("Nome inválido! Deve começar com letra maiúscula e conter apenas letras e espaços.")
            continue
        
        validacaoNome = validaNome(nome)
        if validacaoNome == False:
            print("Nome inválido!")
            continue
        
        validacao = ondeEsta(nome, agd)
        
        if validacao[0]:
            print("Nome já existe! Favor digitar outro...")
            continue
        
        # Restante do cadastro...
        while True:
            aniversario = input("Insira a data de aniversário (DD/MM/AAAA): ")
            if padrao_de_data.match(aniversario):
                diaMesAno = aniversario.split('/')
                validacaoData = validaData(int(diaMesAno[0]), int(diaMesAno[1]), int(diaMesAno[2]))
                if validacaoData == True:
                    break
            else:
                print("Data inválida! Formato esperado: DD/MM/AAAA")
        
        end = input("Insira o endereço: ")
        
        while True:
            telefone = input("Digite o telefone fixo ((xx) xxxx-xxxx ou xxxx-xxxx): ")
            if padrao_de_telefone.match(telefone):
                break
            print("Telefone inválido. Formato esperado: (xx) xxxx-xxxx ou xxxx-xxxx")
            
        while True:
            celular = input("Digite o celular ((xx) 9xxxx-xxxx): ")
            if padrao_de_celular.match(celular):
                break
            print("Celular inválido. Formato esperado: (xx) 9xxxx-xxxx")
            
        email = input("Insira o email: ")
        contato = [nome, aniversario, end, telefone, celular, email]
        agenda.insert(validacao[1], contato)
        
        print("\nCadastro realizado com sucesso!")
        return



def procurar (agd):
    # Ficar pedindo para digitar um nome até digitar um nome que existe cadastrado;
     while True:
        nome = input("Insira um nome ou digite 'Cancela' para sair: ").strip()
        
        if nome.upper() == 'CANCELA':
            print("\nProcura cancelada")
            return
            
        validacao = ondeEsta(nome, agd)
        
        if not validacao[0]:
            print("Nome não encontrado! Tente novamente.")
            continue

        #Usamos validacao[1] para acessar o índice do contato na agenda    
        contato = agd[validacao[1]]

        #Depois, usamos um segundo índice [0], [1] etc. para pegar os dados específicos dentro do contato
        print("\nContato encontrado:")
        print(f"Nome: {contato[0]}")
        print(f"Aniversário: {contato[1]}")
        print(f"Endereço: {contato[2]}")
        print(f"Telefone: {contato[3]}")
        print(f"Celular: {contato[4]}")
        print(f"E-mail: {contato[5]}")
        return
    
    

def atualizar (agd):
    nome_achado = False
    
    while not nome_achado:
        atualiza_nome = input("Insira um nome para ser atualizado ou digite 'Cancela' para sair: ").strip()
        if atualiza_nome.upper() == 'CANCELA':
            print()
            print("Atualização cancelada")
            nome_achado = True
            
        else: #então não foi digitado cancela
            
            if padrao_de_nome.match(atualiza_nome):
                validacao = ondeEsta(atualiza_nome, agd)
                
                if not validacao[0]:
                    print("Nome não encontrado! Tente novamente.")
                    continue
                    
                else:
                    # posição do contato dentro da lista agd
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

                        if opcao == '6':  # Finalizar
                            print("Atualizações concluídas.")
                            return


                        
                        opcao = int(opcao) - 1  # transforma a string em inteiro e ajusta o índice

                        if opcao == 0:  # Aniversário
                            novo_valor = input("Digite o novo aniversário (ou 'cancela' para não alterar): ")
                            if novo_valor.upper() != "CANCELA":
                                agd[indice][1] = novo_valor # nome é 0, niver é 1 ...
                                print("Aniversário atualizado com sucesso.")
                                
                        elif opcao == 1:  # Endereço
                            novo_valor = input("Digite o novo endereço (ou 'cancela' para não alterar): ")
                            if novo_valor.upper() != "CANCELA":
                                agd[indice][2] = novo_valor
                                print("Endereço atualizado com sucesso.")
                                
                        elif opcao == 2:  # Telefone
                            novo_valor = input("Digite o novo telefone (ou 'cancela' para não alterar): ")
                            if novo_valor.upper() != "CANCELA":
                                agd[indice][3] = novo_valor
                                print("Telefone atualizado com sucesso.")
                                
                        elif opcao == 3:  # Celular
                            novo_valor = input("Digite o novo celular (ou 'cancela' para não alterar): ")
                            if novo_valor.upper() != "CANCELA":
                                agd[indice][4] = novo_valor
                                print("Celular atualizado com sucesso.")
                                
                        elif opcao == 4:  # Email
                            novo_valor = input("Digite o novo e-mail (ou 'cancela' para não alterar): ")
                            if novo_valor.upper() != "CANCELA":
                                agd[indice][5] = novo_valor
                                print("E-mail atualizado com sucesso.")
                                
                        elif opcao == 5:  # Finalizar atualização
                            print("Finalizando atualização para esse contato.")
                            return
            else:
                print("Nome inválido! Tente novamente.")
        


    

def listar (agd):
    #Vamos usar um for para percorrer cada item da lista agd.
    #Cada contato é uma outra lista com os seguintes campos: nome, aniversario ... 
    print()

    if len(agd) == 0: #Então essa lista está vazia
        print("Nenhum contato foi cadastrado")
        return

    print ("=========== Lista de contatos cadastrados ===========")

    # Percorre cada contato na agenda, com índice (1, 2, 3...)
    for i, contato in enumerate(agd, start=1):  #contato é cada item da lista agd (ou seja, uma sublista com os dados do contato)
        
        print()  # Espaço entre os contatos
        
        print(f"Contato {i}:")
        print(f"  Nome:        {contato[0]}")
        print(f"  Aniversário: {contato[1]}")
        print(f"  Endereço:    {contato[2]}")
        print(f"  Telefone:    {contato[3]}")
        print(f"  Celular:     {contato[4]}")
        print(f"  E-mail:      {contato[5]}")


    
    

def excluir (agd):
    
     while True:
        excluir_nome = input("Digite o nome a ser excluído ou 'Cancela' para desistir: ").strip()

        if excluir_nome.upper() == 'CANCELA':
            print("Exclusão cancelada.")
            return  # sai da função excluir

        encontrado = False  # flag para saber se achou o nome

        for i in range(len(agd)):   # range(len(agd)) - Gera os índices dos contatos: 0, 1, 2, ..., último
            
            if agd[i][0].upper() == excluir_nome.upper(): #Verifica se o nome do contato é igual ao que foi digitado para ser excluído
                encontrado = True

                # Exibe os dados do contato encontrado
                print("\nContato encontrado:")
                print(f"  Nome:        {agd[i][0]}")
                print(f"  Aniversário: {agd[i][1]}")
                print(f"  Endereço:    {agd[i][2]}")
                print(f"  Telefone:    {agd[i][3]}")
                print(f"  Celular:     {agd[i][4]}")
                print(f"  E-mail:      {agd[i][5]}")

                while True:
                    confirmar = input("\nTem certeza que deseja excluir este contato? (S/N): ").strip().upper()
                    if confirmar == 'S':
                        del agd[i]
                        print("Contato excluído com sucesso!")
                        return  # fim da função após excluir
                    
                    elif confirmar == 'N':
                        print("Exclusão não realizada.")
                        return
                    
                    else:
                        print("Resposta inválida! Digite apenas S ou N.")
                break  # break desnecessário aqui, mas deixado por clareza

        if not encontrado:
            print("Contato não encontrado. Tente novamente.")
            



apresenteSe()

agenda=[] # essa é a listona que  contém as listinhas

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')
