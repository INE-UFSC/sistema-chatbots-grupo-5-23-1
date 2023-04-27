from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome):
        super().__init__(nome,{
            '1': ["Bom dia", "Ih, ah lá...Tá querendo pedir algo, neh?"], 
            '2': ["Qual o seu nome?","Vish, fiz algo de errado?"], 
            '3': ["Quero um conselho","Não faça nada ilegal! Afinal, é errado...e não gostos de coisas erradas! :#"], 
            '4': ["Adeus","Tchau, tchau! Se cuida!...(eita, será que fiz algo de errado?)"]
            })

    @property
    def nome(self):
        return super().nome
    
    @nome.setter
    def nome(self, nome):
        super().nome = nome

    def apresentacao(self):
        return f"Nunca fiz nada de errado, então, não tem o porque me escolher. Mas se quiser, sem problemas!"

    def boas_vindas(self):
        return "Adorei que me escolheu!"

    def despedida(self):
        return "Ufa essa foi por pouco...Quer dizer...Bye!s"
