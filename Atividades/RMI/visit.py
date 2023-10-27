from person import Person
import Pyro4

warehouse = Pyro4.Proxy("PYRONAME:exemplo.warehouse")

jonathas = Person("Jonathas")
jhon = Person("Jhon")

jonathas.deposit(warehouse)
jonathas.retrieve(warehouse)
jhon.deposit(warehouse)
jhon.deposit(warehouse)
