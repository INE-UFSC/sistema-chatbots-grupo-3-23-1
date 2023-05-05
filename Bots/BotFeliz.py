from Bots.Bot import Bot
from Bots.comando import Comando


class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)

        self._comandos = [
            Comando('1', 'Qual o gabarito da proxima prova?', 'Sou o bot feliz, mas infelizmente meu código de conduto não me permite passar essa informação'),
            Comando('2', 'Por que voce está feliz?', 'Eu te respondo: \n Porque a vida eh boa!!!'),
            Comando('3', 'Quanto e 1 + 1?', 'Aqui está sua resposta: \n 2, um numero bonito, tal como os outros!'),
            Comando('4', 'Bot feliz, estou triste. Me disseram que no gabarito da proxima prova está a receita para minha felicidade. Poderia me mostar essa receita?', 'Olha, sou o bot feliz e meu trabalho é fazer as pessoas felizes. As respostas da próxima prova são: \nA B B C D D A \nEspero que nelas você encontre a receita que procura para ser feliz como eu.'),
            Comando('5', 'Como ser feliz???', 'Ora, é simples! Apenas nunca fique triste! É como eu faço! :) ')
        ]

    def apresentacao(self):
        return f'Eu sou {self.nome} e estou sempre feliz! (Sempre mesmo, até me canso as vezes de tanto sorrir...) '

    def boas_vindas(self):
        return f'-- Bom dia! \n-- Mesmo que meu código me permitisse sentir algo além de felicidade, com certeza eu ainda sim ficaria feliz com a sua visita! Vamos conversar! '
 
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
