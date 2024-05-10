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
    print(f'Você escolheu a opção {escolha_usuário} para cadastrar o seu restaurante no nosso sistema, seja bem-vindo!')

elif escolha_usuário == 2:
    print(f'Você escolheu a opção {escolha_usuário} para listar o seu restaurante!')

elif escolha_usuário == 3:
    print(f'Você escolheu a opção {escolha_usuário} para ativar o seu restaurante!')

elif escolha_usuário == 4:
    print(f'Você escolheu a opção {escolha_usuário} para sair do programa.')

else: 
    print(f'Você escolheu a opção {escolha_usuário}. Não temos essa opção!')