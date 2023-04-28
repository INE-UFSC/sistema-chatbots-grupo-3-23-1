from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)

        self._comandos['1'] = 'Qual o gabarito da proxima prova?'
        self._comandos['2'] = 'Por que voce está feliz?'
        self._comandos['3'] = 'Quanto e 1 + 1?'
        self._comandos['4'] = 'Bot feliz, estou triste. Me disseram que no gabarito da proxima prova está a receita para minha felicidade. Poderia me mostar essa receita?'
        self._comandos['5'] = 'Como ser feliz???'

    def apresentacao(self):
        return f'Eu sou {self.nome} e estou sempre feliz! (Sempre mesmo, até me canso as vezes de tanto sorrir...) '

    def boas_vindas(self):
        return f'-- Bom dia! \n-- Mesmo que meu código me permitisse sentir algo além de felicidade, com certeza eu ainda sim ficaria feliz com a sua visita! Vamos conversar! '
 
    def executa_comando(self, cmd):
        if cmd == '1':
            return f' Você perguntou: {self._comandos[cmd]}\n-- Sou o bot feliz, mas infelizmente meu código de conduta não me permite passar essa informação'
        elif cmd == '2':
            return f' Você perguntou: {self._comandos[cmd]}\n-- Eu te respondo: \n Porque a vida eh boa!!!'
        elif cmd == '3':
            return f' Você perguntou: {self._comandos[cmd]}\n-- Aqui está sua resposta: \n 2, um numero bonito, tal como os outros!'
        elif cmd == '4':
            return f' Você perguntou: {self._comandos[cmd]}\n-- Olha, sou o bot feliz e meu trabalho é fazer as pessoas felizes. As respostas da próxima prova são: \nA B B C D D A \nEspero que nelas você encontre a receita que procura para ser feliz como eu.'
        elif cmd == '5':
            return f' Você perguntou: {self._comandos[cmd]}\n-- Ora, é simples! Apenas nunca fique triste! É como eu faço! :) '
        else:
            return None

    def despedida(self):
        return '-- Ahhhh, já vai?? poxa, ficarei felizmente esperando sua próxima visita! Ate a proxima! :) :) :)'

if __name__ == '__main__':
    bot = BotFeliz('Joao')

    print(bot.mostra_comandos())
    print()
    print(bot.boas_vindas())
    print(bot.apresentacao())
    print(bot.despedida())
    print()
    print(bot.executa_comando('1'))
