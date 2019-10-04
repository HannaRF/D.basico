# programação via testes (tdt)
import unittest

class Biblioteca:
    def __init__(self,artigos):
        self.artigos = artigos
        self.autores = set(list(a))
    def get_vizinhos(self,autor):
        art = [t for t in self.artigos if autor in t]
        for a in art:
            v = a[0] if a[1] != autor else a[1]
            viz.append(v)
        return viz
    def get_num_erdos(self,autor):
        if autor in get_vizinhos("erdos"):
            return 1
        else:
            return 2

# assert (condição) se True passa ,se False retorna erro
class TestErdos(unittest.TestCase):
    def SetUp(self):
        self.B = Biblioteca([("francisco","hanna"),("erdos","hanna"),("erdos","francisco")])
    
    def test_verifica_numero_artigos_maior_que_zero(self):
        B = Biblioteca(artigos=[("francisco","leo"),("erdos","hanna")])
        self.assertGreater(len(B.artigos),0) # verifica se a primeira é maior que a primeira

    def test_arg_erdos(self):
        B = Biblioteca(artigos=[("francisco","leo"),("erdos","hanna")])
        a = False
        for i in B.artigos:
            #a = True if ("erdos" in i) else a
            #a = a or ("erdos" in i)
            a |= "erdos" in i
        assert(a)

    def test_são_vizinhos(self):
        viz = self.B.get_vizinhos("joão")
        assert("hanna" in viz)

    def test_numero_1(self):
        assert(self.B.)
    
    def test_existe_lista_autores(self):
        assert("autores" in dir (self.B))
        
        
if __name__ == "__main__":
    unittest.main() # executa os testes e retorna um relatório,com o tempo de execução
