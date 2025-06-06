class Estante():
   def _init_(self):
      self.livros = dict()
   
   def cadastrar(self, livro):
        self.livros[livro.titulo] = livro
   
   def consultar_por_tanana(self):
      pass
   
   def consultar_por_papapa(self):
      pass


class Livro():
    def __init__(self, titulo, n_paginas):
        self.titulo = titulo
        self.n_paginas = n_paginas
        self.n_pg_atual = 0
    def marcar_pagina(self, n_pg_atual):
     self.n_pg_atual = n_pg_atual

    def quant_pg_para_terminar(self):
     qt_pgs = self.n_paginas - self.n_pg_atual
     return qt_pgs

umLivro = Livro("um titulo", 300)
outroLivro = Livro("outro titulo", 50)

umLivro.marcar_pagina(20)
print(umLivro.quant_pg_para_terminar())