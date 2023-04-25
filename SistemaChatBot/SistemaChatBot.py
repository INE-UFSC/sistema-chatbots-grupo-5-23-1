from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        ##mostra mensagem de boas vindas do sistema
        print(f"Bem-vindo ao sistema de chatbots da empresa {self.__empresa}")

    def mostra_menu(self):
        ##mostra o menu de escolha de bots
        print("Selecione um dos bots disponíveis: ")
        for i, bot in enumerate(self.__lista_bots):
            print(f"{i} - Bot: {bot.nome} - Apresentação: {bot.apresentacao()}")
    
    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        escolha = int(input("Digite o número do bot que deseja escolher: "))
        
        while (escolha not in range(len(self.__lista_bots))):
            escolha = input("Insira um número válido: ")
        
        self.__bot = self.__lista_bots[escolha]


    def mostra_comandos_bot(self):
        ##mostra os comandos disponíveis no bot escolhido
        self.__bot.mostra_comandos()


    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        cmd = int(input("Digite o comando desejado (-1 para fechar programa): "))
        self.__bot.executa_comando(cmd)
        return cmd

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.__bot.boas_vindas()
        while True:
            self.mostra_comandos_bot()
            comando = self.le_envia_comando()
            if comando == -1:
                break
        self.__bot.despedida()
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
