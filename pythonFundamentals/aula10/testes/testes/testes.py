from unittest import TestCase, main
from modulo import somar, subtrair, multiplicar, dividir

class testeCalculadora(TestCase):
	def test_soma(self):
		n1 = 10
		n2 = 10
		res = somar(n1,n2)
		self.assertEqual(20,res)

	def test_subtracao(self):
		n1 = 10
		n2 = -20
		res = subtrair(n1,n2)
		self.assertEqual(30,res)
	
	def test_multiplicacao(self):
		n1 = 5
		n2 = 4
		res = multiplicar(n1,n2)
		self.assertEqual(20, res)

	def test_divisao(self):
		n1 = 2
		n2 = 2
		res = dividir(1, res)
		self.assertEqual(1, res)

if __name__ == '__main__':
	main()
