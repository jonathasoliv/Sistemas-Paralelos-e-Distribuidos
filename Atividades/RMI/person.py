class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        print("Aqui eh", self.name)
        self.deposit(warehouse)
        self.retrieve(warehouse)
        print("Obrigado")

    def deposit(self, warehouse):
        print("Armazem contem: ", warehouse.list_contents())
        item = input("Entrem com um intem armazenado: ")
        if item:
            warehouse.store(self.name, item)

    def retrieve(self, warehouse):
        print("Armazem contem: ", warehouse.list_contents())
        item = input("Qual item deseja retirar?: ")
        if item:
            warehouse.take(self.name, item)
