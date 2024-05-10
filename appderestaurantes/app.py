import os
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


def finalizar_programa():
    os.system('cls')
    print('Programa encerrado')

def escolher_opções(escolha_usuário):

    if escolha_usuário == 1 :
        print(f'Você escolheu a opção {escolha_usuário} para cadastrar o seu restaurante no nosso sistema, seja bem-vindo!')

    elif escolha_usuário == 2:
        print(f'Você escolheu a opção {escolha_usuário} para listar o seu restaurante!')

    elif escolha_usuário == 3:
        print(f'Você escolheu a opção {escolha_usuário} para ativar o seu restaurante!')

    elif escolha_usuário == 4:
        finalizar_programa()

    else: 
        print(f'Você escolheu a opção {escolha_usuário}. Não temos essa opção!')

def main():
    exibir_nome_do_app()
    exibir_opções()
    escolha_usuário = int(input('Digite a sua opção: '))
    escolher_opções(escolha_usuário)

if __name__ == '__main__':
    main()
