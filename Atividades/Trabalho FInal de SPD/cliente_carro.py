import xmlrpc.client
import random

##usar o cliente/servidor atual para os ajustes, apresentar sera o oficial
# Cria o proxy do servidor RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Função para verificar e imprimir as vagas disponíveis/ocupadas
def verificar_vagas_disponiveis():
    vagas_disponiveis, vagas_ocupadas = proxy.verificar_vagas()
    if vagas_disponiveis:
        print("\nVagas disponíveis no estacionamento: ", ", ".join(str(vaga) for vaga in vagas_disponiveis))
    else:
        print("Não há vagas disponíveis no estacionamento!")

    if vagas_ocupadas:
        print("Vagas ocupadas no estacionamento: ", ", ".join(str(vaga) for vaga in vagas_ocupadas))
    else:
        print("Não há vagas ocupadas!")

print("******** BEM VINDO AO ESTACIONAMENTO!! ********\n")

print("=== Vagas no início da execução ===")
verificar_vagas_disponiveis()
print("---------------------------------------")

# Simula a entrada de veículos
num_iteracoes = 6  # Defina o número de iterações desejado

for i in range(num_iteracoes):
    print(f"\n-------- Iteração {i+1} ---------")

    #verificar_vagas_disponiveis()

    # Gerar uma lista aleatória de vagas para entrada sendo 10 vagas aleatórias selecionadas entre os números de 1 a 10. 
    vagas_entrada = random.sample(range(1, 11), 10)

    #simula a entrada de veículos em vagas específicas do estacionamento usando o servidor XML-RPC e impresso na tela
    for vaga in vagas_entrada:
        success, mensagem = proxy.entrada_veiculo(vaga)
        if success:
            print(mensagem)
        else:
            print(f"Erro ao tentar a vaga {vaga}: {mensagem}")

        verificar_vagas_disponiveis()

    # Gerar uma lista aleatória de 4 vagas para saída do estacionamento
    vagas_saida = random.sample(vagas_entrada, 4)

    for vaga in vagas_saida:
        success, mensagem = proxy.saida_veiculo(vaga)
        if success:
            print(mensagem)
        else:
            print(f"Erro ao sair da vaga {vaga}: {mensagem}")

        #Sverificar_vagas_disponiveis()

    #print("------------------") 

print("----- ATÉ BREVE! -----")


print("\n=== INFORMACAO DAS VAGAS ATUALIZADO AO FIM DA EXECUCAO ===")

verificar_vagas_disponiveis() #Verificar as vagas disponíveis e ocupadas no final da execução

print("---------------------------------------")
