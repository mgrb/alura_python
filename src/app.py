import os

def print_header() -> None:
   print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
      """)
   
def print_menu()-> None:
   print("""
    --------------------------------
         OPÇÕES DO SISTEMA
    --------------------------------
    1. Cadastrar restaurante
    2. Listar restaurante
    3. Ativar restaurante
    99. Voltar ao menu principal
    0. Sair
      """)
   
def get_opcao()-> int:
  opc: int = 0
  try:
    opc = int(input('Escolha uma opção:'))
    print(f'Você escolheu a opção: {opc}')
  except ValueError:
    print('Opção inválida')
  return opc

def executar_opcao(opcao: int)-> None:
  if opcao == 1:
    print('Cadastrando restaurante')
  elif opcao == 2:
    print('Listando restaurantes')
  elif opcao == 3:
    print('Ativando restaurante')
  elif opcao == 99:
    print('Voltar ao menu principal')
  elif opcao == 0:
    os.system('clear')
    print('Saindo do sistema')
    exit(0)
  else:
    print('Opção inválida')

if __name__ == '__main__':
  opcao: int = 99
  while True:
    if opcao == 99:
      os.system('clear')
      print_header()
    print_menu()
    opcao = get_opcao()
    executar_opcao(opcao)
    
