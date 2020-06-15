from time import sleep


# Decorações

def linha():
    print('-' * 40)


def titulo(txt):
    print('-' * 40)
    print(f'{txt: ^40}')
    print('-' * 40)


def mostra_menu(lista):
    titulo('MENU')
    for op in enumerate(lista):
        print(f'{op[1]:-<10}{op[0]:->10}')
        sleep(0.3)
    linha()


# inputs

def leiaint(x):
    ok = False
    while not ok:
        print(x, end='')
        txt = input('')
        sleep(0.5)
        try:
            txtint = int(txt)
            # print(f'"{txtint}" é um número inteiro válido!')
            return txtint
        except (ValueError, TypeError):
            print(f'"{txt}" NÃO é um número inteiro válido!')
        except (KeyboardInterrupt):
            print(f'"O usuário preferiu interromper o programa.')


def recebe_ordem(lista):
    while True:
        ordem = leiaint('Insira sua opção: ')
        if 0 <= ordem <= (len(lista) - 1):
            return ordem
        else:
            print('Opção inválida, insira uma opção existente no MENU.')
            mostra_menu(lista)


# manipulão de arquivos

def checaarq():
    try:
        open('dados.txt', 'rt')
        return True
    except:
        return False


def criaarq():
    if not checaarq():
        try:
            open('dados.txt', 'wt+')
            print('Arquivo "dados.txt" criado com sucesso')
        except:
            raise Exception('Não foi possível criar o arquivo "dados.txt"')
    else:
        print('Arquivo "dados.txt" já existente')

# articulação


def executar(ordem):
    if ordem == 0:
        titulo('CONSULTAR')
        consultar()
    if ordem == 1:
        titulo('CADASTRAR')
        cadastrar()


# funcionalidades


def consultar():
    arq = open('dados.txt', 'rt')
    for c in arq:
        d = c.split(';')
        d[1] = d[1].replace('\n', '')
        print(f'{d[0]} tem {d[1]} anos')
    sleep(0.5)

def cadastrar():
    nome = input('Insira o nome: ')
    idade = leiaint('Insira a idade')
    arq = open('dados.txt', 'a')
    arq.write(f'{nome};{idade}\n')