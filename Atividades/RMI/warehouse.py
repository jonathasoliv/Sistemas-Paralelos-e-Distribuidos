import Pyro4


@Pyro4.expose  # permitindo o acesso as classes remota
class Warehouse(object):
    def __init__(self):
        self.contents = ["cadeira", "bike", "lampada", "laptop"]

    def list_contents(self):
        return self.contents

    def take(self, name, item):
        self.contents.remove(item)
        print(name, "retirou", item)

    def store(self, name, item):
        self.contents.append(item)
        print(name, "armazenou", item)


def main():
    Pyro4.Daemon.serveSimple(
        {
            Warehouse: "exemplo.warehouse"
        })


if __name__ == "__main__":
    main()
