import threading
import datetime
from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn #permite várias solicitações concorrentes em threads separadas.

class Veiculo:
    def __init__(self, vaga, horario_entrada, letra_carro): 
        self.vaga = vaga
        self.horario_entrada = horario_entrada
        self.horario_saida = None
        self.letra_carro = letra_carro

class Estacionamento:
    def __init__(self, vagas_totais): 
        self.vagas_totais = vagas_totais
        self.vagas_ocupadas = {}
        self.mutex = threading.Lock() # garantir o acesso seguro aos recursos compartilhados como a lista de vagas ocupadas
        self.letras_disponiveis = iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #identificacao dos carros

    def verificar_vagas(self):
        #acesso ao dicionário vagas_ocupadas seja feito de forma segura 
        with self.mutex: 
            vagas_disponiveis = []
            vagas_ocupadas = []
            
            #Se uma vaga estiver presente no dicionário vagas_ocupadas, ela é adicionada à lista vagas_ocupadas. Caso contrario é adicionado na vagas_disponiveis
            for vaga in range(1, self.vagas_totais + 1): 
                if vaga in self.vagas_ocupadas:
                    vagas_ocupadas.append(vaga)
                else:
                    vagas_disponiveis.append(vaga)
            return vagas_disponiveis, vagas_ocupadas
        
    
    def obter_proxima_letra_disponivel(self):
        try:
            return next(self.letras_disponiveis)
        except StopIteration:
            self.letras_disponiveis = iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            return next(self.letras_disponiveis)

    def entrada_veiculo(self, vaga):
        with self.mutex:
            if vaga in self.vagas_ocupadas:
                return False, "Vaga ocupada! Tente novamente"
            elif len(self.vagas_ocupadas) >= self.vagas_totais:
                return False, "Estacionamento lotado!"
            else:
                horario_entrada = datetime.datetime.now()
                letra_carro = self.obter_proxima_letra_disponivel()
                veiculo = Veiculo(vaga, horario_entrada, letra_carro)
                self.vagas_ocupadas[vaga] = veiculo
                
                return True, f"\nCarro {letra_carro} entrou na vaga {vaga} == Horário de entrada: {horario_entrada.strftime('%H:%M:%S')}"

    def saida_veiculo(self, vaga):
        with self.mutex: #verificar se a vaga não está presente no dicionário self.vagas_ocupadas
            if vaga not in self.vagas_ocupadas:
                return False, "Vaga não ocupada."
            else:
                veiculo = self.vagas_ocupadas.pop(vaga)
                horario_saida = datetime.datetime.now()
                tempo_estacionado = horario_saida - veiculo.horario_entrada
                veiculo.horario_saida = horario_saida

                #convertendo o horario para hora, minuto e segundos
                horas = tempo_estacionado.seconds // 3600
                minutos = (tempo_estacionado.seconds // 60) % 60
                segundos = tempo_estacionado.seconds % 60

                return True, "\nCarro {} saiu da vaga {} === Horário de saída: {}. Tempo estacionado: {} horas, {} minutos, {} segundos".format(veiculo.letra_carro, vaga, horario_saida.strftime("%H:%M:%S"), horas, minutos, segundos)

#permite que o servidor RPC execute várias threads para lidar com solicitações concorrentes de clientes XML-RPC.
class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

# iniciar o servidor e processar as solicitações recebidas. Quando uma solicitação é recebida, o servidor a processa e envia a resposta de volta ao cliente.
def handle_request(server):
    print("Estacionamento on-line! Sejam bem vindos!")
    server.serve_forever()

# Cria um objeto Estacionamento com 10 vagas totais
estacionamento = Estacionamento(15)

# Cria o servidor RPC
server = ThreadedXMLRPCServer(("localhost", 8000))
server.register_instance(estacionamento)

# Inicia o servidor em uma thread separada
server_thread = threading.Thread(target=handle_request, args=(server,))
server_thread.start()

# Aguarda o encerramento do servidor
server_thread.join()
