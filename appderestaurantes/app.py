import os
restaurantes = []

def exibir_nome_do_app():
    print('''
        
    █▄▀ █▀█ █▀▄▀█ █ █▀▄ ▄▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    █░█ █▄█ █░▀░█ █ █▄▀ █▀█   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
        ''')

def exibir_opções():
    print('Seja bem-vindo ao Komida Express, o aplicativo perfeito para você gerenciar seu e-restaurante\n ')
    print('O que você deseja fazer?\n')

    print('[1] para cadastrar restaurante')
    print('[2] para listar restaurante')
    print('[3] para ativar restaurante')
    print('[4] para sair\n')

def cadastrar_restaurante():
    os.system('cls')
    print('''
    Seja bem-vindo a área de cadastro de restaurantes!
          ''')
    qnt_restaurante = int(input('\nVocê quer cadastrar quantos restaurantes? '))

    for i in range(1 ,  qnt_restaurante + 1 ):
        restaurante = {}
        restaurante['nome'] = str(input(F'Digite o nome do restaurante: ')) .strip() .upper()
        restaurante['categoria'] = str(input('Digite a categoria do restaurante: ')) .strip() .upper()
        restaurante['ativo'] = True
        print(f'{restaurante['nome'].title()} cadastrado com sucesso!\n')
        restaurantes.append(restaurante)
    voltar_menu()

def listar_restaurante():
    os.system('cls')
    print('Seja bem-vindo a área de listagem dos restaurantes! \n')
    print('Os restaurantes listados são: \n ')

    for restaurante in restaurantes:
        ativado_desativado = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'
        print(restaurante['nome'], '|', restaurante['categoria'], '|', ativado_desativado)

    voltar_menu()

def alterar_estado():
    os.system('cls')
    print('Alterando estado do restaurante!\n')
    nome_restaurante = str(input('Digite o nome do restaurante que queira ativar ou desativar: ')).strip() .upper()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo'] == True:
                print('O restaurante foi ativado com sucesso!\n')
            else:
                print('O restaurante foi desativado com sucesso!\n')

        if not restaurante_encontrado:
            print('O restaurante não foi encontrado!\n')
    voltar_menu()

def voltar_menu():
        input('Digite qualquer tecla para voltar ao menu principal! ')
        main()

def finalizar_programa():
    os.system('cls')
    print('Programa encerrado')

def opção_inválida():
    print('Opção inválida!\n')
    input('Digite qualquer tecla para voltar ao menu principal ')
    main()  # Aqui você chama a função que exibe o menu principal.

def escolher_opções():

    try:
        escolha_usuário = input('Digite a sua opção: ')

        if escolha_usuário == '1':
            cadastrar_restaurante()

        elif escolha_usuário == '2':
            listar_restaurante()

        elif escolha_usuário == '3':
            alterar_estado()

        elif escolha_usuário == '4':
            finalizar_programa()

        else:
            opção_inválida()
      
    except:
        opção_inválida()

def main():
    os.system('cls')
    exibir_nome_do_app()
    exibir_opções()
    
    escolher_opções()

if __name__ == '__main__':
    main()
