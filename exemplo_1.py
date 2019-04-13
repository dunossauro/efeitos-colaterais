from typing import Sized


def tamanho(contavel: Sized) -> int:
    """Conta qualquer coisa contável."""
    return len(contavel)


a = 'Live de Python'
b = tamanho(a)  # 14

assert b == tamanho(a), \
    f'{b} não tem o tamanho correto, esperado {tamanho(a)}'
