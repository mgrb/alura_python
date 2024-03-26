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
    4. Sair
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
  elif opcao == 4:
    print('Saindo do sistema')
    exit(0)
  else:
    print('Opção inválida')

if __name__ == '__main__':
  print_header()
  while True:
    print_menu()
    opcao: int = get_opcao()
    executar_opcao(opcao)
