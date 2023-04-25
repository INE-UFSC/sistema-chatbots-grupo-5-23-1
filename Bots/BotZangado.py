from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome_usuario):
        self.__nome = nome_usuario
        self.__comandos = {1: 'Para quem?', 2: 'Silêncio', 3: 'Pensa com a mente que você mesmo tem um', 4: 'Te manca'}

    @property
    def nome(self):
        return nome

    @nome.setter
    def nome(self, nome_usuario):
        self.nome = nome_usuario

    def apresentacao(self):
        print("Grrrrr. Meu nome é Yoda e eu te odeio!")
 
    def mostra_comandos(self):
        print("1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus")
    
    def executa_comando(self,cmd):
        print(self.__comandos[1])
        print(self.__comandos[2])
        print(self.__comandos[3])
        print(self.__comandos[4])

    def boas_vindas(self):
        print("Ótimo te ver por aqui... mas já pode ir embora!")

    def despedida(self):
        print("Já vai tarde.")