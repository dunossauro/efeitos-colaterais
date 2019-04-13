from typing import Sized


def tamanho(contavel: Sized) -> int:
    """Conta qualquer coisa contável."""
    return len(contavel)


a = 'Live de Python'.split()
b = tamanho(a)  # 3
a.append('side_effect')

assert b == tamanho(a), \
    f'{b} não tem o tamanho correto, esperado {tamanho(a)}'
