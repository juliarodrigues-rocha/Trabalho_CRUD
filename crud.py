'''
Implementar a opções do menu, sempre cuidando de validar os inputs do usuário.
Usar, sempre que cabível, as funções prontas no código.
'''
import re
padrao_de_telefone = re.compile('^(?:\\([0-9]{2}\\) )?9?[0-9]{4}-[0-9]{4}$')
padrao_de_celular = re.compile('^(?:\\([0-9]{2}\\) )?9?[0-9]{5}-[0-9]{4}$')
padrao_de_nome = re.compile('^[A-Z][a-z]*(?: (?:[A-Z]|[a-z])[a-z]*)*$')

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
        
        if nome.upper() == agd[meio][0].upper():
            return [True, meio]
        elif agd[meio][0].upper() < nome.upper():
            inicio = meio + 1 # então o nome esta para a direita, é maior que o meio > 5
        else:
            final = meio - 1 # então o nome esta para a esquerda, é menor que o meio < 5
        
    return [False, inicio] # aqui e caso não ache o nome, então ele nao existe e deve ser inserido nessa posição de inicio
    
    # a função deverá retornar a lista [True,meio] quando encontrar nome procurado ou então a lista [False,inicio], quando não encontrar o nome procurado.
    # busca binária



def cadastrar (agd):
    # print('Opção não implementada!')
    # Ficar solicitando a digitação de um nome de um contato a ser cadastrado na agenda, até que um nome NÃO CADASTRADO seja digitado.
    nome_achado = False
    while not nome_achado:
        digita_nome = input("Insira um nome: ")
        if padrao_de_nome.match(digita_nome) :
            validacao = ondeEsta(digita_nome,agd) #verificando se o nome existe na lista
            if validacao[0] == False: #nome não existe
                nome_achado = True
            else:
                print("Nome já existe! Favor digitar outro.")
        else: 
            print("Nome inválido! Favor digitar novamente...")

 # Solicitar então a digitação do aniversario, do endereço, do telefone (fixo), do celular e do e_mail da pessoa, cujo nome foi digitado. Gerar então uma lista conforme abaixo:
    aniversario = input("Insira a data de aniversário: ")
    end = input("Insira o endereço: ")
    fone = input("Insira o número de telefone fixo: ")
    cel = input("Insira o número de celular: ")
    email = input("Insira o email: ")
    
    contato=[digita_nome,aniversario,end,fone,cel,email] #na listona, 0 é contato
    
    agenda.append(contato) #adicionando a listinha contato na listona agenda         
                
        

    
   
    
                      
    # lembrando que agd é parâmetro formal desta função; o parâmetro real que é fornecido no programa ao chamar esta função se chama agenda.
    # Na listona, as listinhas deverão estar em ordem alfabética de nome e o local apropriadoa para a inserção deverá ser obtido usando a função ondeEsta, que realiza uma busca binária.
    # O usuário poderá desistir de cadastrar, escrevendo "cancela" no
    # momento de digitar o nome a ser cadastrado.
    # A função deverá terminar com uma mensagem informando cadastro
    # realizado com sucesso ou cadastro não realizado.




def procurar (agd):
    # print('Opção não implementada!')
    # Ficar pedindo para digitar um nome até digitar um nome que existe cadastrado;
    nome_achado = False
    while not nome_achado:
        digita_nome = input("Insira um nome ou 'Cancela' para sair da proucura: ")
        if digita_nome.upper() == 'CANCELA':
            print()
            print("Procura cancelada")
            break
        else:
            if padrao_de_nome.match(digita_nome) :
                validacao = ondeEsta(digita_nome, agd) #verificando se o nome existe na lista
                if validacao[0] == False: #nome não existe, então pede o nome novamente
                    print("Nome não existe! Favor digitar outro.")
                else:
                    nome_achado = True # achou o nome, mostra os dados da listinha 
                    
                    print()
                    print('Nome: ',agd[validacao[1]][0])
                    print('Aniversario: ',agd[validacao[1]][1])
                    print('Endereco: ',agd[validacao[1]][2])
                    print('Telefone: ',agd[validacao[1]][3])
                    print('Celular: ',agd[validacao[1]][4])
                    print('E-mail: ',agd[validacao[1]][5])
            else: 
                print("Nome inválido! Favor digitar novamente...")
    
    # mostrar então na tela TODOS os demais dados encontrados sobre aquela pessoa.
    
    # O usuário poderá desistir de procurar, escrevendo "cancela" no  momento de digitar o nome a ser procurado.

def atualizar (agd):
    print('Opção não implementada!')
    # Ficar solicitando a digitação de um nome de um contato a ser
    # atualizado na agenda, até que um nome cadastrado seja digitado.
    # Ficar mostrando então um SUBMENU oferecendo as opções de atualizar
    # aniversário, ou endereco, ou telefone, ou celular, ou email, ou
    # finalizar as atualizações; ficar pedindo para digitar a opção até
    # digitar uma opção válida; realizar a atulização solicitada; tudo
    # isso até ser escolhida a opção de finalizar as atualizações.
    # REPARE que não foi prevista uma opção de atualizar o nome!
    # USAR A FUNÇÃO opcaoEscolhida, JÁ IMPLEMENTADA, PARA FAZER O MENU.
    # O usuário poderá desistir de atualizar, escrevendo "cancela" no
    # momento de digitar o nome a ser atualizado, ou, até mesmo, no
    # momento de digitar o aniversário ou o endereço ou o telefone (fixo)
    # ou o celular ou ainda o e_mail (caso o usuário tenha optado por
    # uma dessas atualizações, naturalmente).

def listar (agd):
    print('Opção não implementada!')
    # implementar aqui a listagem de todos os dados de todos
    # os contatos cadastrados
    # printar aviso de que não há contatos cadastrados se
    # esse for o caso

def excluir (agd):
    print('Opção não implementada!')
    # Ficar solicitando a digitação de um nome a ser excluido da agenda,
    # até que um nome cadastrado seja digitado.
    # Os dados encontrados deveriam então ser mostrados e a exclusão
    # deveria ser confirmada.
    # Sendo confirmada, a exclusão deveria ser realizada e uma mensagem
    # de exclusão bem sucedida deveria ser mostrada. Não sendo confirmada,
    # uma mensagem de exclusão não realizada deveria ser mostrada.
    # O usuário poderá desistir de excluir, escrevendo "cancela" no
    # momento de digitar o nome a ser excluído.
    

    
    
# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa
# (nosso CRUD, C=create(cadastrar), R=read(recuperar),
# U=update(atualizar), D=delete(remover,apagar)




apresenteSe()

agenda=[] # essa é a listona que deverá conter listinhas

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
