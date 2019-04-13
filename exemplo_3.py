"""
Mostrando o problema do print

Como executar:
    python exemplo_3.py > /dev/full
"""
from unittest import mock, TestCase


class TestPrintFunction(TestCase):
    @mock.patch('builtins.print')
    def test_deve_retornar_ola_bb(self, mock_stdout):
        print('Sim, eu sou um problema')
        # import pdb; pdb.set_trace()
        mock_stdout.assert_called_with(
            'Sim, eu sou um problema'
        )


if __name__ == '__main__':
    try:
        print('Sim, eu sou um problema')
    except:
        "????????????????????????"
        open('deu_ruim.txt').write('fudeu')
