print('''
      
█▄▀ █▀█ █▀▄▀█ █ █▀▄ ▄▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
█░█ █▄█ █░▀░█ █ █▄▀ █▀█   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
      ''')


print('Seja bem-vindo ao Komida Express, o aplicativo perfeito para você gerenciar seu e-restaurante\n ')
print('O que você deseja fazer?\n')

print('[1] para cadastrar restaurante')
print('[2] para listar restaurante')
print('[3] para ativar restaurante')
print('[4] para sair\n')

escolha_usuário = int(input('Digite a sua opção: '))

if escolha_usuário == 1 :
    print(f'Você escolheu cadastrar o seu restaurante no nosso sistema, seja bem-vindo!')

if escolha_usuário == 2:
    print(f'Você escolheu listar o seu restaurante!')

if escolha_usuário == 3:
    print(f'Você escolheu ativar o seu restaurante!')