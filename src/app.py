import os

restaurante_repo = [
    'Bonamazza Pizzaria',
    'Brazetos Churrascaria',
    'Casa do Pastel',
    'Casa do Pão de Queijo',
]


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
        opc = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opc}')
    except ValueError:
        print('Opção inválida')
        opc = 99
    return opc


def executar_opcao(opcao: int) -> None:
    os.system('clear')
    match opcao:
        case 1:
            cadastrar_restaurante()
        case 2:
            listar_restaurantes()
        case 3:
            print('Ativando restaurante')
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
        nome_restalrante = input(
            'Digite o nome do restaurante que deseja cadastrar: '
        )
        restaurante_repo.append(nome_restalrante)
        print(f'Restaurante {nome_restalrante} cadastrado com sucesso!')

        cadastrar_restaurante = voltar_menu_principal(
            msg='Deseja cadastrar um restaurante? (s/n): ',
            is_yes_or_no_question=True,
        )

        if not cadastrar_restaurante:
            break


def voltar_menu_principal(
    msg: str = 'Pressione qualquer tecla para voltar ao menu: ',
    is_yes_or_no_question: bool = False,
) -> bool:
    resposta = input(msg)
    avaliacao: bool = True

    if is_yes_or_no_question:
        avaliacao = True if resposta.lower() == 's' else False

    os.system('clear')
    return avaliacao


def listar_restaurantes() -> None:
    print('++++++++++++++++++++++++++')
    print('Listando restaurantes')
    for index, restaurante in enumerate(restaurante_repo):
        print(f'{index + 1}. {restaurante}')

    voltar_menu_principal()


if __name__ == '__main__':
    os.system('clear')
    while True:
        print_header()
        print_menu()
        opcao = get_opcao()
        executar_opcao(opcao)
