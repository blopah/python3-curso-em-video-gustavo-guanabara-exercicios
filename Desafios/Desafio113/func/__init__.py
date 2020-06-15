def leiaint(x):
    ok = False
    while not ok:
        print(x, end='')
        txt = input('')
        try:
            txtint = int(txt)
            print(f'"{txtint}" é um número inteiro válido!')
            ok = True
        except (ValueError, TypeError):
            print(f'"{txt}" NÃO é um número inteiro válido!')
        except (KeyboardInterrupt):
            print(f'"O usuário preferiu interromper o programa.')

def leiafloat(x):
    ok = False
    while not ok:
        try:
            print(x, end='')
            txt = input('')
            try:
                txtfloat = float(txt)
                print(f'"{txtfloat}" é um número real válido!')
                ok = True
            except (ValueError, TypeError):
                print(f'"{txt}" NÃO é um número real válido!')
        except KeyboardInterrupt:
            print(f'"O usuário preferiu interromper o programa.')
