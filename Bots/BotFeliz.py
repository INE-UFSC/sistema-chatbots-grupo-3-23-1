from Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)

        self._comandos['1'] = 'Qual o gabarito da proxima prova?'
        self._comandos['2'] = 'Por que voce esta feliz?'
        self._comandos['3'] = 'Quanto e 1 + 1?'

    def apresentacao(self):
        return f'Eu sou {self.nome}. Me escolha!'

    def boas_vindas(self):
        return f'Bom dia! Que voce ganhe na loteria hoje!'
 
    def executa_comando(self, cmd):
        if cmd == '1':
            return 'A B E E C D E A'
        elif cmd == '2':
            return 'Porque a vida eh boa'
        elif cmd == '3':
            return '2, um numero bonito, igual os outros'
        else:
            return None

    def despedida(self):
        return f'Ate a proxima!'

if __name__ == '__main__':
    bot = BotFeliz('Joao')

    print(bot.mostra_comandos())
    print()
    print(bot.boas_vindas())
    print(bot.apresentacao())
    print(bot.despedida())
    print()
    print(bot.executa_comando('1'))
