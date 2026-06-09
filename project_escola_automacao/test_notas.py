#Importei a biblioteca unittest para programar as chamadas de teste
import unittest

from gerenciador_notas import calcular_media, verificar_aprovacao

class TestSistemaAcademico(unittest.TestCase):

    # 1. Testando as condições normais de aprovação e reprovação
    def test_condicoes_normais(self):
        # Teste de cálculo de média normal
        notas_aluno_aprovado = [8.0, 7.0, 9.0]
        self.assertEqual(calcular_media(notas_aluno_aprovado), 8.0)
        
        notas_aluno_reprovado = [5.0, 6.0, 4.0]
        self.assertEqual(calcular_media(notas_aluno_reprovado), 5.0)

        # Teste de verificação (Média 8.0 deve passar, Média 5.0 deve falhar)
        self.assertTrue(verificar_aprovacao(8.0))
        self.assertFalse(verificar_aprovacao(5.0))

    # 2. Testando o caso extremo: lista de notas totalmente vazia
    def test_lista_vazia(self):
        notas_vazias = []
        # O sistema deve retornar 0.0 sem quebrar (evitando divisão por zero)
        self.assertEqual(calcular_media(notas_vazias), 0.0)

    # 3. Testando o acionamento limitador da função informando zero na  média de corte
    def test_media_minima_zero(self):
        # Se a média mínima for 0, qualquer nota (até mesmo 0.0) deve resultar em aprovação
        self.assertTrue(verificar_aprovacao(0.0, media_minima=0.0))
        self.assertTrue(verificar_aprovacao(5.0, media_minima=0.0))

if __name__ == '__main__':
    unittest.main()