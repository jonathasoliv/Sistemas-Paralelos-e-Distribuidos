import Pyro4
import os
from gtts import gTTS


@Pyro4.expose  # Pyro permite acesso a classe remotas, classes remotas podem solicitar o metodo texttospeech
class caixaDeSom:
    def textToSpeech(self, ptexto):  # metodo que entrego um texto e ele converte em audio
        self.tts = gTTS(text=ptexto, lang='pt')
        self.tts.save("audio123.mp3")  # salvando audio no computador

        # passando o tipo de codec que eu utilizei para a abertura do meu arquivo
        # os.system("groove Audio.mp3")
        os.system("mpg321 audio123.mp3")
        # abre o meu arquivo para reprodução do audio
        os.system('start audio123.mp3')


def main():  # metodo responsavel por colocar o servidor escutando
    Pyro4.Daemon.serveSimple(  # daemon é um processo de fundo
        {  # iniciando o servidor Pyro, registrando o objeto que vai ficar dentro do servidor
            # passa a classe e o nome que sera identificado,reconhecido
            caixaDeSom: "rodando.servidor"
        }#, host= "172.30.30.142")
    )


if __name__ == "__main__":  # se esse arquivo aqui se for apartir dele que tenha inicia a execucao
    main()  # chama o metodo main
