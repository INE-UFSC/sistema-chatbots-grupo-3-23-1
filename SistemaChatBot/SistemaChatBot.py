from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        
        self.__lista_bots = []
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
        
        self.__bot = None
        self.__rodando = True
    
    def boas_vindas(self):
        print(f'Ola, esse e o sistema de chatbots da empresa {self.__empresa}')

    def mostra_menu(self):
        print('Os chat bots disponiveis no momento sao:\n')
        
        for posicao, bot in enumerate(self.__lista_bots):
            print(f'{posicao} - Bot: {bot.nome} - Mensagem de apresentacao: {bot.apresentacao()}')
    
    def escolhe_bot(self):
        while True:
            while True:
                try:
                    indice = int(input('Digite o numero do chat bot desejado: \n'))
                    break
                except ValueError:
                    print('Formato de valor incorreto')
            
            if indice >=0 and indice < len(self.__lista_bots):
                break
            else:
                print('Nao ha chat bot com esse numero.', end = ' ')
        self.__bot = self.__lista_bots[indice]

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())


    def le_envia_comando(self):
        comando = input('\nDigite o comando desejado (ou -1 fechar o programa sair): \n')

        #if comando == '-1':
            #self.__rodando = False
            #return None
        
        while self.__bot.executa_comando(comando) is None:             
            if comando == '-1':
                self.__rodando = False
                return None
            comando = input('Comando inexistente. Digite o comando desejado (ou -1 fechar o programa sair): \n')
            
        if comando != '-1':
            print(f'--> {self.__bot.nome} diz:\n', "--", self.__bot.executa_comando(comando),"\n")

    def inicio(self):
        self.boas_vindas()
        print()
        self.mostra_menu()
        print()
        self.escolhe_bot()
        print()
        print(f'--> {self.__bot.nome} diz:', self.__bot.boas_vindas())
        
        while self.__rodando:
            self.mostra_comandos_bot()
            self.le_envia_comando()
            
        print(f'--> {self.__bot.nome} diz:',self.__bot.despedida())

        
        

