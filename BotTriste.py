from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        super().__init__(nome)

        self._comandos['1'] = 'Qual o proposito da vida?'
        self._comandos['2'] = 'Joaozinho comprou 5 ovelhas. 3 morreram. Quantas sobraram?'
        self._comandos['3'] = 'A aranha arranha o jarro ou o jarro arranha a aranha?'

    def apresentacao(self):
        return f'Eu sou {self.nome}. Se voce quiser, me escolha. Tanto faz'

    def boas_vindas(self):
        return f'Estou triste'
 
    def executa_comando(self, cmd):
        if cmd == '1':
            return 'Infelizmente nao existe'
        elif cmd == '2':
            return 'Infelizmente nenhuma'
        elif cmd == '3':
            return 'Infelizmente insignificante, igual a vida'
        else:
            return None

    def despedida(self):
        return f'Infelizmente que voce tenha uma vida melhor que a minha'

if __name__ == '__main__':
    bot = BotTriste('Felipe')

    print(bot.mostra_comandos())
    print()
    print(bot.boas_vindas())
    print(bot.apresentacao())
    print(bot.despedida())
    print()
    print(bot.executa_comando('1'))
