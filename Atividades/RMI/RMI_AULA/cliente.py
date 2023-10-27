"""import Pyro4
# consulta ao objeto
# fazendo a consulta no nameserver, procura no PYRONAME o meu objto
som = Pyro4.Proxy("PYRONAME:rodando.servidor")
# som contem o endereceo para esse objeto
print("Digite uma mensagem para tocar na caixa de som ")
mensagem = ""
while True:
    if mensagem == "sair":
        sair = "Foi bom conversar com você, até mais!"
        som.textToSpeech(sair)
        break
    else:
        msg = input("Digite sua mensagem aqui: \n")
        som.textToSpeech(mensagem)
"""


import Pyro4

# consulta ao objeto
# fazendo a consulta no nameserver, procura no PYRONAME o meu objeto
som = Pyro4.Proxy("PYRONAME:rodando.servidor")
# som contém o endereço para esse objeto

print("Digite uma mensagem para tocar na caixa de som")
while True:
    mensagem = input("Digite sua mensagem ou digite 'sair' para encerrar:\n")
    if mensagem == "sair":
        sair = "Foi bom conversar com você, até mais!"
        som.textToSpeech(sair)
        break
    else:
        som.textToSpeech(mensagem)