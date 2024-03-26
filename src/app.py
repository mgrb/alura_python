import os


restaurante_repo = []

def print_header() -> None:
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)


def print_menu() -> None:
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


def get_opcao() -> int:
    opc: int = 0
    try:
        opc = int(input('Escolha uma opção:'))
        print(f'Você escolheu a opção: {opc}')
    except ValueError:
        print('Opção inválida')
        opc = 99
    return opc


def executar_opcao(opcao: int) -> None:
    match opcao:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurantes()
        case 3:
            print('Ativando restaurante')
        case 99:
            print('Voltando ao menu principal')
        case 0:
            os.system('clear')
            print('Saindo do sistema')
            exit(0)
        case _:
            print('Opção inválida')

def cadastrar_restaurante() -> None:
    while True:
        print('++++++++++++++++++++++++++')
        print('Cadastrando restaurante')
        nome_restalrante = input('Digite o nome do restaurante que deseja cadastrar: ')
        restaurante_repo.append(nome_restalrante)
        print(f'Restaurante {nome_restalrante} cadastrado com sucesso!')
        cadastrar_restaurante = input('Deseja cadastrar um restaurante? (s/n): ')
        if cadastrar_restaurante.lower() == 'n':
            break

def listar_restaurantes() -> None:
    print('++++++++++++++++++++++++++')
    print('Listando restaurantes')
    for index, restaurante in enumerate(restaurante_repo):
        print(f'{index + 1}. {restaurante}')

if __name__ == '__main__':
    opcao: int = 99
    while True:
        if opcao == 99:
            os.system('clear')
            print_header()
        print_menu()
        opcao = get_opcao()
        executar_opcao(opcao)
