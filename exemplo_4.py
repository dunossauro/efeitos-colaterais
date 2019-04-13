"""
Problema da escolinha.

Faça uma função que pergunte o nome e a idade do usuário e escreva na tela

“Olá <nome>, você tem <idade> anos”

Ahh... Faça usando TDD
"""
from unittest import mock, TestCase


def ola_bb():
    nome = input('BB, me diga seu nome> ')
    idade = input('BB, me diga sua idade> ')
    print(f'Olá {nome}, você tem {idade} anos')


class TestOlaBB(TestCase):
    @mock.patch('builtins.print')
    @mock.patch('builtins.input', side_effect=['Eduardo', '26'])
    def test_ola_bb(self, mock_input, mock_output):
        ola_bb()
        mock_output.assert_called_with('Olá Eduardo, você tem 26 anos')
        
        