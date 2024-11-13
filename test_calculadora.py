# 1) Importar a classe
# "Calculadora"
from calculadora import Calculadora

# 2) Importar o pacote de
# testes unitários chamado "unittest"
import unittest

# 3) Criando a classe de
# testes unitários
class TestCalculadora(unittest.TestCase):

    # 4)Criando o objeto
    # que herdará a classe
    # "Calculadora"

    # OBS: é necessário usar
    # o método chamado "setUp()"
    def setUp(self):
        self.calc = Calculadora()

# 5) Criar o método de teste 
# do método "soma()"
    def test_soma(self):
     self.assertEqual(self.calc.soma(2, 3), 5, "Deve somar dois números")

# Executar a classe de
# testes unitários
if __name__ == '_main_':
    unittest.main()