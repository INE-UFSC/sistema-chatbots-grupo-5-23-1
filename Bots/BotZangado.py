from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().__comandos = {
            1: ["Bom dia", 'Para quem?'], 
            2: ["Qual o seu nome?", 'Silêncio.'], 
            3: ["Quero um conselho", 'Pensa com a mente que você mesmo tem um.'], 
            4: ["Adeus", 'Te manca.']}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print(f"Grrrrr. Meu nome é {self.__nome} e eu te odeio!")

    def boas_vindas(self):
        print("Ótimo te ver por aqui... mas já pode ir embora!")

    def despedida(self):
        print("Já vai tarde.")

    def executa_comando(self,cmd):
        pass

    def mostra_comandos(self):
        pass