from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = list()
        for item in lista_bots:
            self.inclui_bot(item)
        self.__bot = None

    def inclui_bot(self, bot: Bot):
        if isinstance(bot, Bot):
            self.__lista_bots.append(bot)
        return

    #mostra mensagem de boas vindas do sistema
    def boas_vindas(self):
        
        print(f"Bem-vindo ao sistema de chatbots da empresa {self.__empresa}")
    
    #mostra o menu de escolha de bots
    def mostra_menu(self):
        
        print("Selecione um dos bots disponíveis:\n")
        for i, bot in enumerate(self.__lista_bots):
            print(f"{i} - Bot: {bot.nome} - Apresentação: {bot.apresentacao()}")
        
    #faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
    def escolhe_bot(self):
        
        valido = False

        while valido == False:
            try:
                escolha = int(input("Digite o número do bot que deseja escolher:"))
                if escolha in range(len(self.__lista_bots)):
                    valido = True
                    break
                else:
                    print("Insira um número válido!\n")
            except ValueError:
                print("Insira um número válido!\n")

        self.__bot = self.__lista_bots[escolha]

    #mostra os comandos disponíveis no bot escolhido
    def mostra_comandos_bot(self):

        for comando in self.__bot.mostra_comandos():
            print(comando)

    def __imprime_resposta_bot(self, resposta):
        print(f"--> {self.__bot.nome} diz: {resposta}\n")

    #faz a entrada de dados do usuário e executa o comando no bot ativo
    def le_envia_comando(self):

        cmd = input("Digite o comando desejado (-1 para fechar programa): ")
        print()
        if self.__bot.executa_comando(cmd) == None:
            if cmd != '-1':
                print("Interação não encontrada!")
                print()
        else:
            self.__imprime_resposta_bot(self.__bot.executa_comando(cmd))

        return cmd
    
    #mostra mensagem de boas-vindas do sistema
    #mostra o menu ao usuário
    #escolha do bot      
    #mostra mensagens de boas-vindas do bot escolhido
    #entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
    #ao sair mostrar a mensagem de despedida do bot

    def inicio(self):

        self.boas_vindas()
        print()
        self.mostra_menu()
        print()
        self.escolhe_bot()
        print()
        self.__imprime_resposta_bot(self.__bot.boas_vindas())

        while True:
            self.mostra_comandos_bot()
            print()
            comando = self.le_envia_comando()
            if comando == '-1':
                break

        self.__imprime_resposta_bot(self.__bot.despedida())
