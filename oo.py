class Inventario:
    # def add():
    #     ...
    # def alterar(self):
    #     self.__preco = self.__preco*0.9
    #     ...

    def depreciar(self):
        self.__preco = self.preco*0.9
    
    def get_preco(self):
        return self.preco
    def set_preco(self, preco):
        self.__preco = preco 

    def _init_(self, preco, qtd, dep):
        self.__preco = preco
        self.qtd = qtd
        self.dep = dep
# __preco = input("oi: ")
if __name__ == "_main_":
    inventario1 = Inventario(5000, 2, "Pessoal")
    print(inventario1.preco)
    
    inventario1.depreciar()
    print(inventario1.preco)
    