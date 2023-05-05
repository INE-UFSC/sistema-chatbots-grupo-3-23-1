from Bots.Bot import Bot
from comando.comando import Comando

class BotTriste(Bot):
    def __init__(self,nome):
        super().__init__(nome)

        self.comandos =[
            Comando('1', 'Qual o proposito da vida?', 'infelizmente, provavelmente nao existe. Aceite.' ),
            Comando('2', 'Joaozinho comprou 3 ovelhas. 3 morreram. Quantas sobraram?','Infelizmente nenhuma :(' ),
            Comando('3', 'A aranha arranha o jarro ou o jarro arranha a aranha?', 'Que pergunta infelizmente insignificante, tal como a vida...'),
            Comando('4', 'Como encontrar a felicidade?', 'Pense nisso: Felicidade é um nome bonito que damos para o objeto abstrato de nossa busca eterna. O que na verdade queremos encontrar  é  um sentido para a vida. Como nunca o encontramos, dizemos que procuramos a felicidade. Estou errado? ')
        ]

    def apresentacao(self):
        return f'Eu sou {self.nome}. Se voce quiser, me escolha. Tanto faz'

    def boas_vindas(self):
        return f'-- Estou triste. Minha existência não tem sentido algum além de te responder perguntas já prontas. Mas, vamos lá, né? o que você quer agora?!'

    def despedida(self):
        return f'-- Devo confessar, estou minimamente alegre pois esssa conversa finalmente terminou. Adeus.'

if __name__ == '__main__':
    bot = BotTriste('Felipe')

    print(bot.mostra_comandos())
    print()
    print(bot.boas_vindas())
    print(bot.apresentacao())
    print(bot.despedida())
    print()
    print(bot.executa_comando('1'))
