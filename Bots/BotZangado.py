from Bots.Bot import Bot
from Comando.Comando import Comando

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome,[
            Comando('1', "Bom dia", 'Para quem?'), 
            Comando("2", "Qual o seu nome?", 'Silêncio.'),
            Comando("3", "Quero um conselho", 'Pensa com a mente que você mesmo tem um.'),
            Comando("4", "Adeus", 'Te manca.')
            ])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(self, nome):
        super().nome = nome

    def apresentacao(self):
        return f"Grrrrr. Meu nome é {super().nome} e eu te odeio!"

    def boas_vindas(self):
        return "Ótimo te ver por aqui... mas já pode ir embora!"

    def despedida(self):
        return "Já vai tarde."
